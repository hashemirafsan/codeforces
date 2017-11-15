n = int(input())
string = list(str(input()))
zero = 0
one = 0

for i in string:
    if i == '1':
        one += 1
    elif i == '0':
        zero += 1
max_len = max(one, zero)
new_str = ''
i = 0
while i < int(max_len):
    if one == 0 or zero == 0:
        if one >= 1:
           ones = '1' * one
           new_str += ones
        elif zero >= 1:
            zeros = '0' * zero
            new_str += zeros
        break
    else:
        new_str += '10'
        one -= 1
        zero -= 1
    i += 1
print(len(new_str.replace('10', '')))