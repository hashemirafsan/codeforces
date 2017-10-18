n = input()
m = input()
length = len(n)
i = 0
new_str = ''
while i < length:
    if n[i] == '1' and m[i] == '0':
        new_str += '1'
    elif n[i] == '0' and m[i] == '1':
        new_str += '1'
    else :
        new_str += '0'
    i += 1

print(new_str)


