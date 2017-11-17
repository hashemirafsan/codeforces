n = int(input())
arr = list(map(int, input().split()))
if n > 2:
    count = 0
    i = 1
    while i < n-1:
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            count += 1
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1
        i += 1
    print(count)
else:
    print(0)