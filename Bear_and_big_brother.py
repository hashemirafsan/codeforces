a, b = map(int, input().split())
i = 0
count = 0
while i < 1:
    if a <= b:
        a = a * 3
        b = b * 2
        i += 0
        count += 1
    else:
        i += 1

print(count)