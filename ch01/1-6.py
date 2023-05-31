def function(s: str):
    curr_ch = s[0]
    cnt = 1
    result_str = ""

    for i in range(1, len(s)):
        if s[i] != curr_ch:
            result_str += curr_ch + str(cnt)
            curr_ch = s[i]
            cnt = 1
        else:
            cnt += 1

    result_str += curr_ch + str(cnt)

    if len(s) < len(result_str):
        return s
    else:
        return result_str


if __name__ == "__main__":
    print(function(s="aabcccccaaa"))
