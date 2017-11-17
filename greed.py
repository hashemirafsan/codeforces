n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = sorted(b)
d = b.pop()
e = b.pop()
c = [d,e]
print('YES' if sum(c) >= sum(a) else "NO")