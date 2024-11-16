# 2343. 기타 레슨

# 블루레이 크기(size)에 강의를 다 담을 수 있는지 확인하는 함수
def canFit(videos, m, size):		# M은 블루레이 갯수
    count = 1		# 사용한 블루레이 개수를 세는 변수
    current_sum = 0		# 현재 블루레이에 담긴 강의 길이 합계
    
    for video in videos:		# 강의를 순서대로 탐색 후 블루레이에 추가하는 for문
        if current_sum + video > size:		# 현재 블루레이에 이 강의를 추가했을 때 크기를 초과하는 경우
            count += 1		# 새 블루레이를 사용
            current_sum = video		# 새로운 블루레이에 현재 강의를 담음
        else:
            current_sum += video		# 현재 블루레이에 강의를 추가
    return count <= m		# 사용된 블루레이 개수가 M 이하: 현재 size로 M개의 블루레이로 강의 담기가 가능함

# 이진 탐색을 이용하여 블루레이 최소 크기를 찾는 함수
def minimum(videos, m):
	start = max(videos)  # 최소 크기: 가장 긴 강의의 길이 (이보다 작으면 가장 긴 강의를 담을 수 없음)
    end = sum(videos)  # 최대 크기: 모든 강의를 한 개의 블루레이에 담는 경우
    
    while start <= end:
        middle = (start + end) // 2		# 중간값을 현재 블루레이 크기로 설정
        if canFit(videos, m, middle):		# M개의 블루레이에 모든 강의를 담을 수 있는지를 확인
            end = middle - 1		# 범위를 줄임
        else:
            start = middle + 1		# 범위를 늘림
            
    return start  # 탐색 끝: 최소 블루레이 크기 반환

n, m = map(int, input().split())		# n: 강의 수, m: 사용할 블루레이 개수
videos = list(map(int, input().split()))		# 각 강의의 길이 

print(minimum(videos, m))		# 최소 블루레이 크기 출력
