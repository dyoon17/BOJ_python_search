# 1920. 수 찾기

# 이진 탐색 -> X라는 정수의 존재 여부 확인
def binary_search(arr, target):  # 정렬된 정수 배열과 정수 값 정의
    left, right = 0, len(arr) - 1  # 탐색 범위를 설정 (좌측 포인터와 우측 포인터 초기화)
    while left <= right:  
        middle = (left + right) // 2  # 중간 값 계산
        if arr[middle] == target:  # 중간 값이 대상 값과 같은 겅우
            return True  
        elif arr[middle] < target:  # 중간 값이 대상 값보다 작을 경우
            left = middle + 1  # 좌측 포인터를 오른쪽으로 이동
        else:  # 중간 값이 대상 값보다 클 경우
            right = middle - 1  # 우측 포인터를 왼쪽으로 이동
    return False  # 값을 찾지 못하면 False를 반환

n = int(input())  # 배열 A의 크기 입력
array_a = sorted(map(int, input().split()))  # 배열 A를 입력받아 정렬

m = int(input())  # 탐색할 숫자의 개수 입력
array_b = map(int, input().split())  # 탐색할 숫자들 입력

# 각 숫자가 배열 A에 존재하는지 확인
print('\n'.join('1' if binary_search(array_a, num) else '0' for num in array_b))  # 결과 출력
