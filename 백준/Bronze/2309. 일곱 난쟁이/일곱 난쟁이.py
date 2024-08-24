'''
9명에서 2명을 제외하면 더 깔끔
'''
# 입력 받기
heights = [int(input()) for _ in range(9)]

# 전체 키의 합 계산
total_height = sum(heights)

# 두 명의 난쟁이를 제외했을 때 합이 100이 되는지 확인
for i in range(9):
    for j in range(i + 1, 9):
        if total_height - (heights[i] + heights[j]) == 100:
            # 제외할 두 난쟁이를 찾은 경우
            fake1, fake2 = heights[i], heights[j]
            heights.remove(fake1)
            heights.remove(fake2)
            break
    if len(heights) == 7:
        break

# 결과 출력 (오름차순 정렬)
heights.sort()
for height in heights:
    print(height)