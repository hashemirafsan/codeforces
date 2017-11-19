r = 0
n = -1
i = 1
while i < 6:
    a = list(map(int, input().split()))
    if 1 in a:
        r = i
        n = a.index(1)
        n += 1
    i += 1
move = 0
if n <= 3:
    move += 3 - n
else:
    move += n - 3

if r <= 3:
    move += 3 - r
else:
    move += r - 3

print(move)