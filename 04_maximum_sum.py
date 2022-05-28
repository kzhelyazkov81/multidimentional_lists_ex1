def submatrix_sum(matrix, start_row, start_column):
    result = 0
    for i in range (start_row, start_row+3):
        for j in range(start_column, start_column+3):
            result += matrix[i][j]
    return result


def submatrix(matrix, start_row, start_column):
    result = []
    for row in range(start_row, start_row+3):
        result.append(matrix[row][start_column:start_column+3])
    return result

rows, columns = [int(x) for x in input().split(' ')]

matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(' ')])


maximum_sum = float('-inf')
max_submatrix = []
for subrow in range(rows-2):
    for subcolumn in range(columns-2):
        sub_sum = submatrix_sum(matrix, subrow, subcolumn)
        if sub_sum > maximum_sum:
            maximum_sum = sub_sum
            max_submatrix = submatrix(matrix, subrow, subcolumn)

print(f'Sum = {maximum_sum}')
for row in max_submatrix:
    print(' '.join(str(x) for x in row))
