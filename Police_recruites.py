n = int(input())
m = list(map(int, input().split()))
crime = 0
police = 0
i = 0
while i < n:
    if m[i] > 0:
        police += m[i]
    else:
        if police:
            police += m[i]
        else:
            crime += 1

    i += 1
print(crime)