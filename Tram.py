n = int(input())
i = 0
last_persons = 0
arr = []
while i < n:
    a, b = map(int, input().split())
    if i == 0:
        last_persons = b
        arr.append(last_persons)
    else:
        last_persons = (last_persons - a) + b
        arr.append(last_persons)
    i += 1

print(max(arr))


