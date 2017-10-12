arr = []
str = input()
str = str.lower()
newStr = ''
for i in list(range(0, len(str))) :
	if(str[i] != 'a' and str[i] != 'e' and str[i] != 'i' and str[i] != 'o' and str[i] != 'u' and str[i] != 'y') :
		arr.append(".")
		arr.append(str[i])
for i in list(range(0, len(arr))) :
	newStr += ''.join(arr[i])
print(newStr)