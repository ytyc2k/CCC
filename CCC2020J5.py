'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9

'''

R = int(input())
C = int(input())
Matrix = [list(map(int, input().split())) for i in range(R)]

# import time
#
# t1 = time.time()
# Matrix = []
# with open('j5.07.02.in') as f:
#     R = int(f.readline())
#     C = int(f.readline())
#     for i in f:
#         Matrix.append(list(map(int, i.split())))
# print(R, C)
# print(Matrix[0][0])

Stack = [Matrix[0][0]]
Ext = R * C
Ha = [False for _ in range(1000*1000)]
while Stack:
    P = Stack.pop(0)
    if P == Ext:
        print('yes')
        break
    for x in range(1, R + 1):
        if P % x == 0:
            for y in range(1, C + 1):
                if x * y == P:
                    V = Matrix[x - 1][y - 1]
                    if Ha[V-1] == False:
                        Stack.append(V)
                        Ha[V-1] = True
else:
    print('no')
# print(time.time() - t1)
