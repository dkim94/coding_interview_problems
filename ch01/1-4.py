from collections import defaultdict


# def is_palindrome_permutation(string: str):
#     string = string.replace(' ', '').lower()
#     hash_table = defaultdict(int)
#     for ch in string:
#         hash_table[ch] += 1
#     print(string)
#
#     if len(string) % 2 == 0:
#         for key in hash_table.keys():
#             if hash_table[key] % 2 != 0:
#                 return False
#         return True
#     else:
#         cnt = 0
#         for key in hash_table.keys():
#             if hash_table[key] % 2 != 0:
#                 if cnt == 0:
#                     cnt = cnt + 1
#                 else:
#                     return False
#         return True
#

# replace int with bool
def is_palindrome_permutation(string: str):
    string = string.replace(' ', '').lower()
    hash_table = defaultdict(bool)
    for ch in string:
        hash_table[ch] = not hash_table[ch]
    print(string)

    if len(string) % 2 == 0:
        for key in hash_table.keys():
            if hash_table[key]:
                return False
        return True
    else:
        cnt = True
        for key in hash_table.keys():
            if hash_table[key]:
                if cnt:
                    cnt = not cnt
                else:
                    return False
        return True


if __name__ == "__main__":
    print(is_palindrome_permutation(string="Tact Coa"))
    print(is_palindrome_permutation(string="Tact CoaO"))
    print(is_palindrome_permutation(string="Tact CoaL"))
