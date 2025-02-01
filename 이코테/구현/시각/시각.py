n = int(input())
# clock_include_3 = [3, 13, 23]
# count = 0
# for clock in range(n+1):
#     if clock in clock_include_3:
#         count += 60*60
#     else:
#         count += (45*15 + 15*60)

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1 
print(count)
