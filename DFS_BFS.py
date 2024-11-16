# 1260. DFS와 BFS

from collections import deque

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V 입력
n, m, v = map(int, input().split())

list = [[0] * (n + 1) for _ in range(n + 1)]  # 정점 간의 연결 관계를 나타내는 2차원 리스트 생성
visited_dfs = [False] * (n + 1)  # DFS 탐색 시 각 정점을 방문했는지 여부 저장
visited_bfs = [False] * (n + 1)  # BFS 탐색 시 각 정점을 방문했는지 여부 저장

for _ in range(m):
    x, y = map(int, input().split())    # 간선 연결 정보를 입력
    list[x][y] = list[y][x] = 1  # 양방향 간선이므로 양쪽 값을 1로 설정


def dfs(v):  # DFS: 현재 정점을 방문하고 출력함
    visited_dfs[v] = True    
    print(v, end=' ')    
  
    for i in range(1, n + 1):    # 정점 번호가 작은 순서대로 방문하기 위해 1부터 n까지 순회
        if not visited_dfs[i] and list[v][i] == 1:    # 방문하지 않은 연결된 정점인 경우
            dfs(i)    

def bfs(v):    # BFS: 큐를 사용하여 탐색을 진행함
    queue = deque([v])  # 탐색을 시작할 정점을 큐에 추가
    visited_bfs[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
      
        for i in range(1, n + 1):
            if not visited_bfs[i] and list[current][i] == 1:    # 방문하지 않았고 연결된 정점인 경우
                queue.append(i)    # 방문하지 않은 정점을 큐에 추가
                visited_bfs[i] = True

dfs(v)    # DFS 탐색 결과를 출력
print()   # 줄 바꿈
bfs(v)    # BFS 탐색 결과를 출력
