import math
x, N = map(int, input().strip().split())
total_planes_needed = math.ceil(N / 100)
planes_to_purchase = max(0, total_planes_needed - x)
print(planes_to_purchase)
