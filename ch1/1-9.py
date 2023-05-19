def function(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    s2 += s2
    return isSubstring(s1, s2)


def isSubstring(s1: str, s2: str):
    return s1 in s2


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(function(s1=s1, s2=s2))

    s3 = "waterbottle"
    s4 = "notwaterbottle"
    print(function(s1=s3, s2=s4))

    s5 = "waterbottle"
    s6 = "beerbottle"
    print(function(s1=s5, s2=s6))
