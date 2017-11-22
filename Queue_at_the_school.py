n, t = map(int, input().split())
s = list(str(input()))
while t:
    m = 0
    while m < n-1:
        if s[m] == 'B' and s[m+1] == 'G':
            a, b = m, m + 1
            s[a], s[b] = s[b], s[a]
            m += 2
        else:
            m += 1
    t -= 1
print("".join(s))