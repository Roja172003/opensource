def count_divisible_by_3_or_5():
    n = int(input())
    count_3 = n // 3
    count_5 = n // 5
    count_15 = n // 15
    result = count_3 + count_5 - count_15
    print(result)
count_divisible_by_3_or_5()    
