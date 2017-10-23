n,m = map(int, input().split())
arr = []
digit = 1
for i in range(1, n+1):
    small_arr = []
    j = digit
    loop_length = digit + m
    while j < loop_length:
        small_arr.append(j)
        digit += 1
        j += 1
    arr.append(small_arr)

output = 0
k = 0
while k < n:
    if len(arr[0]) == 1:
        output += 1
        break
    else:
        x = [row[1:] for row in arr]
        x = x[1:]
        arr = x
        output += 1
    k += 1

print('Akshat' if output % 2 == 1 else 'Malvika')