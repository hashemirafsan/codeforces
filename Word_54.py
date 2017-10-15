n = input()
l = len(n)
i = 0
upper = 0 
result = ''
while i < l :
	if(n[i].isupper()) :
		upper += 1
	i += 1
lower = l - upper
if(upper == lower) :
	result = n.lower()
elif(upper > lower) :
	result = n.upper()
elif(lower > upper) :
	result = n.lower()
print(result)