from pathlib import Path
import struct

class Database:
    def __init__(self, filename: str):
        self.filename = filename
        self.page_size = 256

    def __enter__(self):
        file_path = Path(self.filename)
        if not file_path.exists():
            with open(file_path, 'x'):
                pass
            self.file_handle = open(file_path, 'rb+')
            self.init_metadata()
        else:
            self.file_handle = open(file_path, 'rb+')

        metadata = self.read_page(0)
        magic_bytes, version, root_page, bitmap = self.parse_metadata(metadata)

        if magic_bytes != b"MYDB":
            raise ValueError(f"Invalid database file format: '{magic_bytes}'")

        self.version = version
        self.root_page = root_page
        self.bitmap = bytearray(bitmap)
        self.allocated_pages = self.count_allocated_pages(bitmap)

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file_handle.close()

    def count_allocated_pages(self, bitmap):
        total = 0
        for val in bitmap:
            total += val.bit_count()
        return total

    def init_metadata(self):
        self.version = 1
        self.root_page = 0
        self.bitmap = bytearray(b'\x00' * 128)

        self.update_metadata_on_disk()

    def parse_metadata(self, data):
        try:
            magic_bytes = data[0:4]
            version = struct.unpack('B', data[4:5])[0]
            root_page = struct.unpack('i', data[5:9])[0]
            bitmap = data[9:137]

            print(f"Magic bytes: {magic_bytes}")
            print(f"Version: {version}")
            print(f"Root page: {root_page}")
            print(f"Bitmap: {bitmap}")

            return magic_bytes, version, root_page, bitmap
        except Exception as e:
            raise ValueError(e)

    def write_page(self, page_number: int, data):
        if (data_size := len(data)) != self.page_size:
            raise ValueError(f"Data is of size {data_size}, but needs to be of size {self.page_size}")

        if page_number < 0:
            raise ValueError(f"Page number '{page_number}' is invalid")

        offset = page_number * self.page_size

        self.file_handle.seek(offset)
        self.file_handle.write(data)

    def read_page(self, page_number: int):
        if page_number < 0:
            raise ValueError(f"Page number '{page_number}' is invalid")

        offset = page_number * self.page_size

        self.file_handle.seek(offset)
        data = self.file_handle.read(self.page_size)
        return data

    def allocate_page(self):
        for i, byte in enumerate(self.bitmap):
            for j in range(8):
                is_set = (byte >> j) & 1
                if not is_set:
                    new_value = byte | (1 << j)
                    self.bitmap[i] = new_value
                    self.allocated_pages += 1
                    self.update_metadata_on_disk()
                    return 8 * i + j + 1
        raise ValueError("Bitmap full")

    def update_metadata_on_disk(self):
        magic_bytes = b"MYDB"
        version = struct.pack('B', self.version)
        root_page = struct.pack('i', self.root_page)
        bitmap = bytes(self.bitmap)
        padding = b'\x00' * 119

        updated_metadata = magic_bytes + version + root_page + bitmap + padding
        self.write_page(0, updated_metadata)

    def release_page(self):
        pass


if __name__ == "__main__":
    with Database("test.db") as db:
        print(f"Initial allocated pages: {db.allocated_pages}")
        page1 = db.allocate_page()
        page2 = db.allocate_page()
        page3 = db.allocate_page()

        print(f"Allocated pages: {page1}, {page2}, {page3}")
        print(f"Total allocated: {db.allocated_pages}")
