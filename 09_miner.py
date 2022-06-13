def movement(command, row, col):
    movements = {
        'up': [row-1, col],
        'down': [row+1, col],
        'left': [row, col-1],
        'right': [row, col+1]
    }
    new_row, new_col = movements[command]
    if 0 <= new_row < size and 0 <= new_col < size:
        row, col = new_row, new_col
    return row, col

size = int(input())
commands = [x for x in input().split(' ')]
matrix = []

for row in range(size):
    matrix.append([x for x in input().split(' ')])

coals_count = 0
miner_row = 0
miner_col = 0
for row in matrix:
    for ch in row:
        if ch == 's':
            miner_row = matrix.index(row)
            miner_col = row.index(ch)
        if ch == 'c':
            coals_count += 1

end = False
for command in commands:
    miner_row, miner_col = movement(command, miner_row, miner_col)
    if matrix[miner_row][miner_col] == 'c':
        coals_count -= 1
        matrix[miner_row][miner_col] = '*'
        if coals_count == 0:
            break
    if matrix[miner_row][miner_col] == 'e':
        end = True
        break

if end:
    print(f'Game over! ({miner_row}, {miner_col})')
else:
    if coals_count == 0:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
    else:
        print(f"{coals_count} pieces of coal left. ({miner_row}, {miner_col})")
