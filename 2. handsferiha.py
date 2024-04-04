
a, b = input().split()
c, d = input().split()

if (a == b or c == d) or (a == d or c == b):
    print('YES')
else:
    print('NO')
    
