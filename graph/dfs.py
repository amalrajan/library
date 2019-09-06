def dfs(u):
    visited[u] = True

    print(u, end=' ')

    for neighbour in adj[u]:
        if not visited[neighbour]:
            dfs(neighbour)


v, e = list(map(int, input().split()))

adj = [[] for _ in range(v)]
visited = [False] * (v)

for i in range(e):
    a, b = list(map(int, input().split())) 
    adj[a].append(b)
    adj[b].append(a)

    # Assuming the graph is undirected.

for i in range(v):
    if not visited[i]:
        dfs(i)
