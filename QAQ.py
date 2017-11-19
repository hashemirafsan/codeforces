import itertools
string = list(str(input()))
m = []

for j in string:
    if j == 'Q' or j == 'A':
        m.append(j)

string = "".join(m)

arr = list(itertools.combinations_with_replacement(string, 3))

count = 0

for i in arr:
    if "".join(i) == 'QAQ':
        count += 1

print(count)