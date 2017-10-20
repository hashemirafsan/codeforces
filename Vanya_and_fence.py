n,h = map(int, input().split())
height = list(map(int, input().split()))
i = 0
width = 0
while i < n:
    if height[i] <= h:
        width += 1
    else:
        width += 2
    i += 1

print(width)