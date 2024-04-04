
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
m = int(input())
for i in range(m):
    a = input()
    if a == 'H':
        lst = lst[::-1]
    elif a == 'V':
        for j in lst:
            lst[lst.index(j)] = j[::-1]
    else:
        lst2 = []
        for h in range(len(lst)):
            r = ''
            for k in range(len(lst[h])):
                r = lst[k][h]+r
            lst2.append(r)
        lst = lst2
for i in lst:print(i)
