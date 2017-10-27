n = int(input())
moves = [1,2,3,4,5]
k = 0
while n:
    i = 4
    while i >= 0:
        if n >= moves[i]:
            n -= moves[i]
            k += 1
            break
        i -= 1
print(k)