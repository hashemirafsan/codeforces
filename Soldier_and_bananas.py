k,n,w = map(int, input().split())
l = (((w*(w+1))//2)*k) - n
print(l if l > 0 else 0)