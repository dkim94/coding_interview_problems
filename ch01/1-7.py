def ninety_degrees_rotate(arr: list):
    new_arr = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    # 1. New array
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         new_arr[i][j] = arr[len(arr) - 1 - j][i]
    # return new_arr

    # 2. Without new array
    n = 0
    N = len(arr)
    while n < N / 2:
        print(n, N / 2)
        for i in range(n, N - 1 - n):
            print(f"swap [{n}][{i}] and [{i}][{N - 1 - n}]")
            arr[n][i], arr[i][N - 1 - n] = arr[i][N - 1 - n], arr[n][i]
            print(arr)

            print(f"swap [{N - 1 - i}][{n}] and [{n}][{i}]")
            arr[N - 1 - i][n], arr[n][i] = arr[n][i], arr[N - 1 - i][n]
            print(arr)

            print(f"swap [{N - 1 - n}][{N - 1 - i}] and [{N - 1 - i}][{n}]")
            arr[N - 1 - n][N - 1 - i], arr[N - 1 - i][n] = arr[N - 1 - i][n], arr[N - 1 - n][N - 1 - i]
            print(arr)
            print()
        n += 1

    return arr


if __name__ == "__main__":
    # print(ninety_degrees_rotate(arr=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    # print(ninety_degrees_rotate(arr=[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]))
    print(ninety_degrees_rotate(arr=[
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]))
