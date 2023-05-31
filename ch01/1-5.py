def function(a: str, b:str):
    cnt = 0
    if len(a) - len(b) >= 2 or len(b) - len(a) >= 2:
        return False
    elif len(a) == len(b):
        for idx in range(len(a)):
            if a[idx] != b[idx]:
                if cnt == 0:
                    cnt += 1
                else:
                    return False
        return True
    else:
        if len(a) < len(b):
            shorter, longer = a, b
        else:
            shorter, longer = b, a
        i = 0
        j = 0
        while i < len(longer) and j < len(shorter):
            if longer[i] != shorter[j]:
                if cnt == 0:
                    cnt += 1
                    i += 1
                else:
                    return False
            i += 1
            j += 1
        return True


if __name__ == "__main__":
    print(function(a="pale", b="ple"))
    print(function(a="pales", b="pale"))
    print(function(a="pale", b="bale"))
    print(function(a="pale", b="bake"))
    print(function(a="abcd", b="efgh"))

