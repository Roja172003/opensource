s = input().strip()
result = ""
n = len(s)
i = 0
while i < n:
    count = 1
    while i + 1 < n and s[i] == s[i + 1]:
        count += 1
        i += 1
    result += s[i] + str(count)
    i += 1
print(result)    
