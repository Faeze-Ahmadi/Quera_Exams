
a = []
while True:
    temp = int(input())
    a.append(temp)
    if temp == 0:
        a.remove(0)
        break
for i in range(len(a))[::-1]:
    print(a[i])



