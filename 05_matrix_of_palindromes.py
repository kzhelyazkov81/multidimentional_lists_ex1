def word(current_row, current_col):
    result = chr(current_row + ord('a')) + chr(current_col + current_row + ord('a')) + chr(current_row + ord('a'))
    return result


r, c = [int(x) for x in input().split(' ')]
matrix = []

for row in range(r):
    matrix_row = []
    for col in range(c):
        matrix_row.append(word(row, col))
    matrix.append(matrix_row)

for row in matrix:
    print(' '.join(row))
