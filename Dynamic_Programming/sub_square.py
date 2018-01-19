# sub square

matrix = [[False] * 4] * 4

matrix[0][0] = matrix[0][1] = matrix[1][0] = matrix[1][1] = True


def sub_square(mat, x, y):
    if x == 4 or y == 4:
        return 0

    if mat[x][y] is False:
        return 0

    count = min(sub_square(mat, x, y + 1),
                sub_square(mat, x + 1, y + 1),
                sub_square(mat, x + 1, y)
                )

    return count + 1


print(sub_square(matrix, 0, 0))
