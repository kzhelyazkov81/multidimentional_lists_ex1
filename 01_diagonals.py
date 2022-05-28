size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - i - 1])

primary_diagonal_str = ', '.join(str(x) for x in primary_diagonal)
primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_str = ', '.join(str(x) for x in secondary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

print(f"Primary diagonal: {primary_diagonal_str}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {secondary_diagonal_str}. Sum: {secondary_diagonal_sum}")
