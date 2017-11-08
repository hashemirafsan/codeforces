n = int(input())
output = []

arr = list(map(int, input().split()))
max_burle = max(arr)
need_burle = 0
i = 0
while i < n:
    if arr[i] < max_burle:
        need_burle += max_burle - arr[i]
    i += 1
output.append(need_burle)
for i in output:
    print(i)