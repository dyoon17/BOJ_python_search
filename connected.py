# 11724. 연결 요소의 개수

def connected(n, edges):
    graph = [[] for _ in range(n + 1)]        # 정점의 개수 n+1만큼 빈 리스트를 생성 -> 각 정점이 연결된 다른 정점들을 저장
    
    for _ in range(len(edges)):        
        u, v = map(int, input().split())  # 간선의 양 끝점 u, v 입력
        graph[u].append(v)  # 정점 u에 연결된 정점 v 추가
        graph[v].append(u)  # 정점 v에 연결된 정점 u 추가

    visited = [False] * (n + 1)  # 각 정점을 방문했는지 여부를 기록하는 리스트 생성

    # DFS 함수 정의
    def dfs(node):
        stack = [node]  # 현재 탐색 중인 노드를 스택에 추가
        while stack:  
            current = stack.pop()  # 스택에서 현재 노드를 꺼내서
            for neighbor in graph[current]:  # 현재 노드와 연결된 이웃 노드 탐색
                if not visited[neighbor]:  # 방문하지 않은 노드일 경우
                    visited[neighbor] = True  
                    stack.append(neighbor)  # 스택에 추가

    count = 0  # count: 연결 요소의 개수를 저장하는 변수
    for i in range(1, n + 1): 
        if not visited[i]:  # 방문하지 않은 정점일 경우
            visited[i] = True  
            dfs(i)  
            count += 1  # 연결 요소의 개수 1 증가

    return count  # 최종 연결 요소의 개수 반환

# 정점(n)과 간선(m)의 개수를 입력받음
n, m = map(int, input().split())
# 연결 요소의 개수를 출력
print(connected(n, [(0, 0)] * m))
