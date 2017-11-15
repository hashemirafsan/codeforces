n = int(input())
string = list(str(input()))
anton = 0
danik = 0

for i in string:
    if i == 'A':
        anton += 1
    elif i == 'D':
        danik += 1

if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
elif anton == danik:
    print('Friendship')