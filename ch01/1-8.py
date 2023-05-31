def set_to_zero_1(arr: list):
    # time O(MN)
    # space O(M+N): row can have max M, col can have max N values

    M = len(arr)
    N = len(arr[0])

    rows, cols = [], []
    for i in range(M):
        for j in range(N):
            if i in rows and j in cols:
                continue
            if arr[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for r in rows:
        for j in range(N):
            arr[r][j] = 0
    for c in cols:
        for i in range(M):
            arr[i][c] = 0

    return arr


def set_to_zero_2(arr: list):
    # time O(MN), but 상수배는 더 클 것 같은
    # space O(1): only two additional variables

    M = len(arr)
    N = len(arr[0])

    first_row_has_zero = False
    first_col_has_zero = False

    # check if first row and col has zero
    for i in range(M):
        if arr[i][0] == 0:
            first_col_has_zero = True
            break

    for j in range(N):
        if arr[0][j] == 0:
            first_row_has_zero = True
            break

    # check arr from second row and col
    # if zero exists, change first row and col value to 0
    for i in range(1, M):
        for j in range(1, N):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0

    # use first row/col value to set remaining values in row/col to 0
    for i in range(M):
        if arr[i][0] == 0:
            for j in range(1, N):
                arr[i][j] = 0

    for j in range(N):
        if arr[0][j] == 0:
            for i in range(1, M):
                arr[i][j] = 0

    if first_row_has_zero:
        for i in range(M):
            arr[i][0] = 0

    if first_col_has_zero:
        for j in range(N):
            arr[0][j] = 0

    return arr


if __name__ == "__main__":
    arr = [
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
    ]

    print(set_to_zero_1(arr=arr))
