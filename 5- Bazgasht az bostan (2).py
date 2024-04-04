

x, y = list(map(int,input().split()))
x1, y1 = list(map(int,input().split()))

if x1 >= x and y1 <= y:
    print('Right')
elif x1 <= x and y1 >= y:
    print('Left')
elif x1 >= x and y1 >= y:
    print('Right')
elif x1 <= x and y1 <= y:
    print('Left')
