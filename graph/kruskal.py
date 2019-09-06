def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph, nodes):
    result = []

    i = 0
    e = 0

    graph = sorted(graph, key=lambda item: item[2])

    while e < nodes - 1:
        u, v, w = graph[i]
        i = i + 1

        x = find(u)
        y = find(v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(x, y)

    for edge in result:
        print(edge)


nodes, edges = list(map(int, input().split()))

parent = list(range(nodes))
rank = [0] * nodes
graph = []

for i in range(edges):
    u, v, w = list(map(int, input().split()))
    graph.append([u, v, w])

kruskal(graph, nodes)
