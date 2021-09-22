# lst=['hello',12,345,[12,[12,34],34]]
# a=lst[3][1][0]
# print(type(lst))
# lst=lst+[50]
# print(lst)
lst=[1,3,2,3,3]
# lst.append(50)
# lst.pop(-1)
# lst.remove(3)
lst[0]=(12,34)
print(lst)
# [100,3,2,3,3]
# 数据类型
# 增加，删除，修改

k=0
for i in range(1,11):
    print(i)
    for j in range(1,11):
        print(i,j)
        if j==2:
            k=1
            break
    if k==1:
        k=0
        break
else:
    print('good')


