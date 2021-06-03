import sys
import collections


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def DFS(u, res):
    stack = [u]

    while stack:
        node = stack.pop()
        res.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                stack.append(nei)
    
    return res

graph = collections.defaultdict(list)
edges = [(1, 0), (0, 2), (2, 1), (0, 3), (1, 4)]
N = 5

for x, y in edges:
    graph[x].append(y)

res = []
visited = set()

for i in range(N):
    if i not in visited:
        visited.add(i)
        DFS(i, res)

print(res)
