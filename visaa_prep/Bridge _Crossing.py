x, y, z = map(int, input().split())
if z < y:
    n = 0
else:
    n = (z - y) // x
print(n)    
