
k = int(input())
k2 = k
for i in range(9):
    if i == 8:
        print('#' * 23)
    elif i % 2 == 0 and i < 7:
        print('#' * 8  + '.' * 7 + '#' * 8)
    else:
        if k > 0:
            print('#ghorfe' + str((-k) + (k2 + 1)), end='')
            k -= 1
        else:
            print('#' + '.' * 7, end='')
        print('.' * 7, end='')
        if k > 0:
            print('ghorfe' + str((-k) + (k2 + 1)) + '#')
            k -= 1
        else:
            print('.' * 7 + '#')
    
    

