'''
그냥 새로운 리스트 하나 더 만듦 ..ㅋㅋ
'''
# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 최종 줄 서는 순서를 담을 리스트
result = []

# 학생 번호는 1부터 시작하므로, enumerate로 인덱스+1을 이용
for i, num in enumerate(numbers):
    # 해당 번호만큼 앞에 삽입
    result.insert(i - num, i + 1)

# 결과 출력
print(" ".join(map(str, result)))
