n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
k = x.pop(0)
x = sorted(x)
l = y.pop(0)
y = sorted(y)
j = list(set(x + y))
if(len(j) == n) :
	print("I become the guy.")
else :
	print("Oh, my keyboard!")