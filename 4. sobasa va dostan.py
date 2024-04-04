
n, a, b = list(map(int, input().split()))
minutes = [int(i) for i in input().split()]
time1 = 45 + a
time2 = 90 + b
ty = 0
tu = 0
i = 0
j = 1

while j < len(minutes):
    if (minutes[j] < minutes[j - 1]) and (minutes[j - 1] - minutes[j]) > a:
        ty = 1
    j += 1
while j < len(minutes):
    if minutes[j] >= 45 and minutes[j] <= minutes[j - 1] and minutes[j] < time1:
        i += 1
        if i > 1:
            ty = 1
    j += 1

j = 0
while j < len(minutes):
    if 0 <= minutes[j] <= time2:
        tu = 0
    else:
        tu = 1
    j += 1

if ty + tu == 0:
    print('YES')
else:
    print('NO')
