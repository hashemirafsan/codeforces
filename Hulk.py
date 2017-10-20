n = int(input())
i = 1
hate = 'I hate '
love = 'I love '
one_line = ''
while i <= n:
    if i == n:
        if i % 2 == 1:
            one_line += hate + 'it'
        else:
            one_line += love + 'it'
    else:
        if i % 2 == 1:
            one_line += hate + 'that '
        else:
            one_line += love + 'that '
    i += 1

print(one_line)