m = list(str(input()))
n = 0
for i in m:
    if i == '4' or i == '7':
        n += 1
print("YES" if n == 4 or n == 7  else "NO")