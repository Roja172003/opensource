x = int(input())
t = x
s = 0
while t != 0:
    d = t % 10
    s += d
    t //= 10
if s % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
