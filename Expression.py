a = int(input())
b = int(input())
c = int(input())
arr = []
firstEx = a + b * c
arr.append(firstEx)
secondEx = a * (b + c)
arr.append(secondEx)
thirdEx = a * b * c
arr.append(thirdEx)
fourEx = (a + b) * c
arr.append(fourEx)
fiveEx = a + b + c
arr.append(fiveEx)
arr.sort()
print(arr[4])