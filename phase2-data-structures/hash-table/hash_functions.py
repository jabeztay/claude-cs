def simple_string_hash(string, prime=31, length=3):
    output = 0
    for i in range(min(len(string), length)):
        output += ord(string[i]) * prime ** (length - 1 - i)

    return output
