n = int(input())
letters = [['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'],['m','n','o'],['p','q','r','s'], ['t','u','v'],['w','x','y','z']]
last_items = ['c','f','i','l','o','s','v','z']
letter_value = [[1,2,3], [1,2,3], [1,2,3], [1,2,3],[1,2,3],[1,2,3,4], [1,2,3],[1,2,3,4]]
result = []
while n:
    string = str(input())
    length = len(string)
    i = 0
    count = 0
    while i < length:
        j = 0
        last_items_length = len(last_items)

        while j < last_items_length:
            if string[i] == ' ':
                count += 1
                break
            elif last_items[j] >= string[i]:
                count += letter_value[j][letters[j].index(string[i])]
                break
            j += 1
        i += 1
    result.append(count)
    n -= 1

index = 1
for item in result:
    print('Case #'+str(index)+': '+str(item))
    index += 1
