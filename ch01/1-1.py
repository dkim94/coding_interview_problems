# with hash table
def find_duplicate(input_str: str):
    char_dict = {}

    for ch in input_str:
        if ch in char_dict.keys():
            return False
        else:
            char_dict[ch] = True

    return True

# without any data structure
# -> compare within string (or sort first & compare with neighbor)


if __name__ == "__main__":
    str_list = [
        "abcdef",
        "abcdefa",
        "aa"
    ]
    for str_ in str_list:
        print(find_duplicate(str_))
