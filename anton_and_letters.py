m = list(map(str, input().split(",")))
n = ''
for i in m:
    i = i.replace('{','')
    i = i.replace('}','')
    n += i
data = list(set(n))
count = 0
for i in data:
    if i != ' ':
        count += 1
print(count)