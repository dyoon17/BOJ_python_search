# 11724. 연결 요소의 개수

def count_connected_components(n, edges):
    from collections import defaultdict, deque

    # 그래프 생성
    # defaultdict를 사용하여 리스트 형태로 각 노드의 인접 노드를 저장하는 그래프를 생성합니다.
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # 노드 u에 연결된 노드 v 추가
        graph[v].append(u)  # 노드 v에 연결된 노드 u 추가 (무방향 그래프이므로 양방향 추가)

    # 방문 체크 리스트
    # 각 노드가 방문되었는지 확인하기 위한 리스트. 초기값은 False로 설정
    visited = [False] * (n + 1)

    # BFS(너비 우선 탐색) 함수 정의
    def bfs(start):
        queue = deque([start])  # 탐색을 위한 큐 생성 및 시작 노드 삽입
        visited[start] = True  # 시작 노드 방문 처리
        while queue:  # 큐가 빌 때까지 반복
            node = queue.popleft()  # 큐에서 노드를 하나 꺼냄
            for neighbor in graph[node]:  # 현재 노드에 연결된 모든 인접 노드 확인
                if not visited[neighbor]:  # 방문하지 않은 노드라면
                    visited[neighbor] = True  # 방문 처리
                    queue.append(neighbor)  # 큐에 추가

    # 연결 요소 개수 카운트
    connected_components = 0  # 연결 요소의 개수를 저장할 변수

    # 모든 노드에 대해 연결 요소 탐색
    for node in range(1, n + 1):  # 1번 노드부터 n번 노드까지 반복
        if not visited[node]:  # 현재 노드가 방문되지 않았다면
            bfs(node)  # BFS 탐색 수행
            connected_components += 1  # 연결 요소 개수 증가

    return connected_components  # 최종 연결 요소 개수 반환

# 입력 처리
if __name__ == "__main__":
    import sys
    input = sys.stdin.read  # 표준 입력을 읽어옴
    data = input().splitlines()  # 입력 데이터를 줄 단위로 분리

    # 첫 줄에서 노드 수 n과 간선 수 m을 읽음
    n, m = map(int, data[0].split())

    # 간선 데이터를 읽어 튜플 리스트로 변환
    edges = [tuple(map(int, line.split())) for line in data[1:]]

    # 연결 요소 개수 계산 및 출력
    print(count_connected_components(n, edges))  # 결과 출력
