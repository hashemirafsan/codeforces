n = int(input())
ax = []
ay = []
az = []
while n:
    x,y,z = map(int, input().split())
    ax.append(x)
    ay.append(y)
    az.append(z)
    n -= 1
print("YES" if sum(ax) == 0 and sum(ay) == 0 and sum(ay) == 0 else "NO")
