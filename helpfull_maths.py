m = str(input())
print('+'.join(sorted(m.split('+'))) if len(m) > 0 else m)