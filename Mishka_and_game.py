n = int(input())
mishka = 0
chris = 0
i = 0
while i < n:
    m,c = map(int, input().split())
    if m > c:
        mishka += 1
    elif c > m:
        chris += 1
    i += 1

if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print('Friendship is magic!^^')