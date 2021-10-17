mat = [[1,2], [3,4]]
n = len(mat)

rotated = []
for i in range(n):
    temp = list()
    for j in range(n-1,-1,-1):
        temp.append(mat[j][i])
    rotated.append(temp)

print(rotated)