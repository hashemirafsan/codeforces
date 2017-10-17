n = int(input())
m = list(map(int,input().split()))
sereja = 0
dima = 0
i = 1
for item in range(0,n) :
	if(m[0] > m[n-1]) :
		if(i%2 == 1) :
			sereja += m[0]
		else :
			dima += m[0]
		index = m.index(m[0])
		del m[index]
	else :
		if(i%2 == 1) :
			sereja += m[n-1]

		else :
			dima += m[n-1]
		index = m.index(m[n-1])
		del m[index]

	i += 1
	n -= 1
	
print(sereja,dima)