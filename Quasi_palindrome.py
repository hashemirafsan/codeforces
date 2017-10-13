t = input()
if(t == t[::-1]) :
	print('YES')
else :
	t = t[::-1]
	i = 0
	m = len(t)
	count = 0
	str = ''
	while i < m :
		if(t[i] == '0') : 
			count += 1
		elif (int(t[i]) > 0): 
			break
		i += 1

	for k in list(range(0,count)) :
		str = '0' + str

	str = str + t[::-1]
	
	if(str == str[::-1]) :
		print('YES')
	else :
		print('NO')