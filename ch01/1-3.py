def change_whitespace(input:str, strlen: int):
    new_str = []
    for c in input:
        if c == ' ':
            new_str.append("%20")
        else:
            new_str.append(c)
    return ''.join(new_str)


if __name__ == "__main__":
    print(change_whitespace("Mr John Smith", 13))
