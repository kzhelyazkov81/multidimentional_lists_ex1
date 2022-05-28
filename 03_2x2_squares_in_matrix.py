def find_square(matrix, start_row, start_col):
    ul = matrix[start_row][start_col]
    ur = matrix[start_row][start_col + 1]
    dl = matrix[start_row + 1][start_col]
    dr = matrix[start_row + 1][start_col + 1]
    if ul == ur == dl == dr:
        return True


row, col = [int(x) for x in input().split(' ')]
matrix = []
for _ in range(row):
    matrix.append([x for x in input().split(' ')])

squares_found = 0
for start_row in range(row - 1):
    for start_col in range(col - 1):
        if find_square(matrix, start_row, start_col):
            squares_found += 1

print(squares_found)
