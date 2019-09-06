def bfs(u):
    visited[u] = True

    q = [u]

    while q != []:
        node = q.pop()
        print(node, end=' ')

        for neighbour in adj[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

v, e = list(map(int, input().split()))

adj = [[] for _ in range(v)]
visited = [False] * v

for i in range(e):
    a, b = list(map(int, input().split()))

    adj[a].append(b)
    adj[b].append(a)

bfs(0)
