n = int(input())
last = 0
for i in list(range(1,n+1)) :	
	for j in list(range(1,i+1)) :
		last += j
	if(last > n) : 
		print(i-1)
		break
	elif(last == n) :
		print(i)
		break
	elif(n == 1) :
		print(1)
		break
