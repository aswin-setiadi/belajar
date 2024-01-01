# write a function takes input 2 int n and m
# this function return a matrix of nxm
# matrix should be filled up with zero


def main(n: int, m: int):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    return matrix


def main2(n: int, m: int):
    # * operator multiply same obj, hence when changing matrix[0][0] it will change the first column in all row
    return list([[0] * m]) * n


# done after interview
def main3(n: int, m: int):
    def _rec(row: list[int]):
        if len(row) < m:
            row.append(0)
            _rec(row)
        return row

    def _rec_row(mat: list[list[int]]):
        if len(mat) < n:
            mat.append(_rec([]))
            _rec_row(mat)
        return mat

    matrix = []
    # while len(matrix) < n:
    #     matrix.append(_rec([]))

    # return matrix
    return _rec_row(matrix)


# # turn the function into recursive
# def main3(n: int, m: int):
#     matrix = []

#     def _rec(index):
# if len==n:
#     return acu_list
# else:
#     acu_list.append(0)
#     return _rec(n-1, acu_list)
#         if index != m - 1:
#             _rec(index + 1)
#         else:
#             matrix.append(0)

#     _rec(0)

# queue -> trigger lambda

if __name__ == "__main__":
    a = main2(3, 4)
    # print(type(a[0]))
    # print(type(a[0][0]))
    for row in a:
        row[0] = 1
        break
    print(a)

    print("recursive solution (done after interview):")
    matrix = main3(3, 4)
    print(matrix)
