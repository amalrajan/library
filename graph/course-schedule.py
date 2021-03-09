import sys
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Solution:
    def canFinish(self, n: int, prereq) -> bool:
        graph = defaultdict(set)
        indegree = [0] * n

        for y, x in prereq:
            graph[x].add(y) 
            indegree[y] += 1

        q = [i for i in range(n) if not indegree[i]]

        for u in q:
            for x in graph[u]:
                indegree[x] -= 1
                if not indegree[x]:
                    q.append(x)

        return len(q) == n

s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))

