x, y, z = map(int, input().split())
gym_only_cost = x
gym_with_trainer_cost = x + y
if z >= gym_with_trainer_cost:
    print(2)
elif z >= gym_only_cost:
    print(1)
else:
    print(0)
    
