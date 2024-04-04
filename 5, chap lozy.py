

n = int(input())

for i in range(n):
    print((n - i) * " " + (((i + 1) * 2) - 1) * "*")
print(((2 * n) + 1) * "*")
for j in range(n):
    print((j + 1) * " " + (2 * n - (((j + 1) * 2) - 1)) * "*" )
