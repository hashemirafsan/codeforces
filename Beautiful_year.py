n = int(input())
i = 0
while i < 1:
    n += 1
    if len(set(str(n))) == 4:
        print(n)
        i += 1
    else:
        i += 0