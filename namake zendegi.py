
n, k = list(map(int, input().split()))
summation = 0
summation2 = 0
for i in range(n):
    temp = [int(j) for j in input().split()]
    summation += temp[-1]
    summation2 += temp[0]
if summation >= k and not(summation2 == summation):
    print('YES')
else:
    print('NO')
    
    
