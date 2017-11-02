n,x = map(int, input().split())
count = 0
i = 1
while i < n + 1:
    if x % i == 0:
        if x / i <= n:
            count += 1
    i += 1
print(count)