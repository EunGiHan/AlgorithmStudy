### DFS 예시 코드
def dfs(graph, v, visited):
    """
    (param)   graph : 그래프 상태가 연결리스트로 저장됨
              v : 노드 번호
              visitied: 방문한 곳을 True로 설정한 1차원 리스트
    """
    
    visited[v] = True   # 현재 노드 방문 처리
    print(v, end = ' ') # 방문하고 있는 노드 출력

    for i in graph[v]:
        # 이 노드와 연결된 노드들을 탐색. i는 인접한 노드의 번호

        if not visited[i]:
            dfs(graph, i, visited)  # 방문하지 않은 노드는 방문

### BFS 예시 코드
from collections import deque

def bfs(graph, start, visited):
    """
    (param)   graph : 그래프 상태가 연결리스트로 저장됨
              start : 
              visitied: 방문한 곳을 True로 설정한 1차원 리스트
    """
    queue = deque([start])  # 큐에 가장 처음 노드를 넣어둔다
    visited[start] = True   # 처음 노드의 방문처리를 한다

    while queue:    # 큐가 차있을 때까지(비지 않을 때까지) 반복
        v = queue.popleft() # 큐에서 원소 하나를 꺼냄
        print(v, end=' ')

        for i in graph[v]:  # 한 노드에 대해
            if not visited[i]:  # 인접 노드를 방문하지 않았다면
                queue.append(i) # 큐에 넣고
                visited[i] = True   # 방문처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4 , 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]   # i 번째 노드에 연결된 노드 번호가 연결리스트로 이루어져 있음. 0번째 노드는 없으므로 빈칸

visited = [False] * 9   # 방문 여부 저장할 1차원 리스트. 노드 개수(0까지 포함해야 하니 노드 개수+1)만큼 선언

dfs(graph, 1, visited)
bfs(graph, 1, visited)