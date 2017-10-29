m = str(input())
n = '47'
complete_list = []
for current in range(3):
    a = [i for i in n]
    for y in range(current):
        a = [x+i for i in n for x in a]
    complete_list = complete_list + a

k = False
l = True
i = 0
length = len(complete_list)
while i < length:
    if complete_list[i] == m:
        l = False
        print('YES')
        break
    else:
        if int(m) % int(complete_list[i]) == 0 or int(m) % int(complete_list[i]) == 0:
            k = True
            break
    i += 1
if l:
    print("YES" if k else "NO")