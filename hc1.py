A = [[[8,3,4],[1,5,9],[6,7,2]],[[8,1,6],[3,5,7],[4,9,2]],[[6,7,2],[1,5,9],[8,3,4]],
     [[6,1,8],[7,5,3],[2,9,4]],[[2,7,6],[9,5,1],[4,3,8]],[[2,9,4],[7,5,3],[6,1,8]],
     [[4,3,8],[9,5,1],[2,7,6]],[[4,9,2],[3,5,7],[8,1,6]]]
matrix = []
new = []
matrix = []
for i in range(3):
    a = [int(i) for i in input().split()]
    matrix.append(a)
print(matrix)
for k in range(8):
    a = 0
    for i in range(3):
        for j in range(3):
            cost = 0
            cost = cost + abs(matrix[i][j]-A[k][i][j])
            print(cost)
            a = a + cost
            print(a)
    new.append(a)
    print(new)
print(new)
min = new[0]
for x in new:
    if(min > x):
        min = x
print(min)
