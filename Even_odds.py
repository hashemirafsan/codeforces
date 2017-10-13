import math
m = input()
m = m.split(" ")
n = int(m[0])
k = int(m[1])

if(n % 2 == 0) :
	odd = even = int(n / 2)
else :
	odd = math.ceil(n/2)
	even = math.floor(n/2)

if(k > odd) :
	l = ((k - odd) * 2)
	print(l)
elif(k == odd) :
	l = ((odd - 1) * 2 ) + 1
	print(l) 
else :
	l = ((k - 1) * 2) + 1 
	print(l)
