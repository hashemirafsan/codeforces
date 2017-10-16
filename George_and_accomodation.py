n = int(input())
i = 0
count = 0
while i < n :
	p,q = map(int,input().split())
	q = q - 2
	if(q >= p) :
		count += 1
	i += 1
print(count)