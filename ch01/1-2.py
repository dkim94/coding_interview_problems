# def is_permutation_of(str_1: str, str_2: str):
#     sorted_1 = sorted(str_1)
#     sorted_2 = sorted(str_2)
#
#     return sorted_1 == sorted_2

def is_permutation_of(str_1: str, str_2: str):
    hash_table = {}
    for c in str_1:
        if c not in hash_table.keys():
            hash_table[c] = 0
        hash_table[c] += 1

    for c in str_2:
        if c not in hash_table.keys():
            return False
        hash_table[c] -= 1
        if hash_table[c] < 0:
            return False

    for key in hash_table.keys():
        if hash_table[key] > 0:
            return False

    return True


if __name__ == "__main__":
    str1 = "abcdef"
    str2 = "cdafeb"
    print(is_permutation_of(str1, str2))

    str3 = "abcdef"
    str4 = "aabbcc"
    print(is_permutation_of(str3, str4))
