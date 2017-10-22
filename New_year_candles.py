a, b = map(int, input().split())
hours = 0
remind = 0
while a > 0:
    remind = a
    a -= b
    if a <= 0:
        hours += remind
    else:
        hours += b
    a += 1
print(hours)