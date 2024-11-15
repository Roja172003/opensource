N, x, y = map(int, input().split())
if y % x == 0 and y // x <= N:
    print("YES")
else:
    print("NO")
