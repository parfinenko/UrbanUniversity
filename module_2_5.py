def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        row = []

    for p in range(m):
        row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(5,4,10)
result2 = get_matrix(1,2,1)
result3 = get_matrix(1,2,1)

print(result1)
print(result2)
print(result3)