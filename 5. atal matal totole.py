
a = input().split()
n, k = int(a[0]), int(a[1])

b = n
lst = []
c = 1
for i in range(1, n + 1):
    lst.append(i)
    lst.append(i)
while b != 1:
    print(lst[0], end=' ')
    lst = lst[1:] + lst[1:]
    if c == k:
        c = 0
        lst.pop()
        print()
    c += 1
    b = len(set(lst))
print(f'winner:{f[0]}')
