# https://toph.co/p/gpa-calculator
# GPA Calculator
# Limits: 1s, 512 MB

# Shibli is a very good student. He is very regular and attentive in his classes. 
# He is very serious about his study. So he makes good result in every semester. 
# Recently his previous semester result has published. 
# Since Shibli is very busy with his study he asks his 
# good friend Swapnil who is a very good programmer to calculate his Grade Point Average (GPA).

# Input

# Input starts with an integer T(<=5), denoting the number of test cases. 
# Each test case starts with an integer N(<=8), 
# denoting the number of subjects. Next N 
# line contains a floating point number p (2 ≤ p ≤ 4) denoting the grade point 
# Shibli got in each subject of previous semester. And you can assume that p contains four digits after the decimal point.

# Output

# For each test case, print a line “Case x: y” where x is replaced by the test case number 
# and y is the GPA of previous semester Shibli got, rounded to three places after the decimal point.


n = int(input())
i = 0
j = 0
total = 0
arr = []
while i < n :
	m = int(input())
	while j < m :
		o = float(input())
		total += o
		j += 1
	total  = total / m
	total = round(total, 3)
	arr.append(total)
	i += 1
	j = 0
	total = 0
index = 1
for i in arr :
	print('Case '+ str(index) +': ' + str(i))
	index += 1