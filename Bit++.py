n = int(input())
X = 0
i = 0
while i < n:
    cmd = input()
    if cmd == 'X++' or cmd == '++X':
        X += 1
    else:
        X -= 1
    i += 1

print(X)