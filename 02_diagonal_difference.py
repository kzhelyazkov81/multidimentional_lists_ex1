size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(x) for x in input().split(' ')])

diagonal_sum = 0

for i in range(size):
    diagonal_sum += matrix[i][i] - matrix[i][size - i - 1]

print(abs(diagonal_sum))
