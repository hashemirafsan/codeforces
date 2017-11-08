player = str(input())
p_len = len(player)
if p_len > 7:
    if '0000000' in player:
        print('YES')
    elif '1111111' in player:
        print('YES')
    else:
        print('NO')
else:
    print('NO')