rows, cols = [int(x) for x in input().split(' ')]

matrix = []

for row in range(rows):
    matrix.append([x for x in input().split(' ')])

valid = True
while True:
    if not valid:
        print('Invalid input!')
    valid = True
    command = input().split(' ')
    if command[0] == 'END':
        break
    if len(command) != 5:
        valid = False
        continue
    if command[0] != 'swap':
        valid = False
        continue
    r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
    if r1 < 0 or r1 > rows-1 or c1 < 0 or c1 > cols-1 or r2 < 0 or r2 > rows-1 or c2 < 0 or c2 > cols-1:
        valid = False
        continue
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    for row in matrix:
        print(' '.join(row))
