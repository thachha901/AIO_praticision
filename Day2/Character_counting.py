def characterCounting(string):
    string = string.lower()  # Convert to lowercase for case-insensitive counting
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


if __name__ == "__main__":
    test_string = "HELlo world"
    result = characterCounting(test_string)
    print(f"Character count for '{test_string}': {result}")