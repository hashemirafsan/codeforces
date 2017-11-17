lower,upper = map(int, input().split())
prime = []

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            prime.append(num)
if len(prime) > 1:
    print("YES" if prime[1] == upper else "NO")
else:
    print("NO")