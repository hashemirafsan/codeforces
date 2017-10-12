n = int(input())
arr = []
m = 0
k = 0
temp = 0
while m < n :
	str = input()
	str = str.split(' ')
	for i in str :
	 	if(int(i) == 1) :
	 		temp += 1

	if(temp > 1) :
		k += 1

	temp = 0
	m += 1
print(k)