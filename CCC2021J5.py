'''
4
5
7
R 3
C 1
C 2
R 2
R 2
C 1
R 4

hello
10
'''

R = int(input())
C = int(input())
N = int(input())

Matrix = [[False for _ in range(C)] for j in range(R)]
Ra = [False for _ in range(R)]
Ca = [False for _ in range(C)]

for i in range(N):
    T = input().split()
    if T[0] == 'R':
        Ra[int(T[1])-1] = not Ra[int(T[1])-1]
    else:
        Ca[int(T[1])-1] = not Ca[int(T[1])-1]

for i in range(R):
    if Ra[i]:
        for j in range(C):
            Matrix[i][j] = not Matrix[i][j]
for i in range(C):
    if Ca[i]:
        for j in range(R):
            Matrix[j][i] = not Matrix[j][i]

CountTrue = 0
for i in range(R):
    CountTrue += Matrix[i].count(True)
print(CountTrue)
