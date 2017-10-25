n,m = map(int, input().split())
leftOrRight = True
for i in range(1,n+1):
    string = ''
    if i % 2 == 1:
        for t in range(1,m+1):
            string += '#'
    else:
        if leftOrRight:
            for t in range(1,m+1):
                if t == m:
                    string += '#'
                else:
                    string += '.'
            leftOrRight = False
        else:
            for t in range(1,m+1):
                if t == 1:
                    string += '#'
                else:
                    string += '.'
            leftOrRight = True

    print(string)