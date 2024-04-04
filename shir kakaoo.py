
n = int(input())
i = list(map(int, input().split()))

summation = 0
a = 0

for j in range(len(i)):
    summation -= i[j]
    if summation < 0:
        a += abs(summation)
        summation = 0
print(a)
