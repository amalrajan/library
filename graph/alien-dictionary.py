import sys
import heapq
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def topological_sort(graph):
    q = []
    for c in graph.keys():
        if indegree[ord(c) - ord('a')] == 0:
            q.append(c)

    res = ''

    while q:
        c = q.pop(0)
        res = res + c + " "

        for nei in graph[c]:
            indegree[ord(nei) - ord('a')] -= 1
            if indegree[ord(nei) - ord('a')] == 0:
                q.append(nei)

    return res


words = ["baa", "abcd", "abca", "cab", "cad"]
# words = ['caa', 'aaa', 'aab']
words_count = len(words)

indegree = [0] * 26
visited = [0] * 26

graph = defaultdict(set)
for i in range(words_count - 1):
    w1, w2 = words[i], words[i + 1]

    for j in range(min(len(w1), len(w2))):
        if w1[j] != w2[j] and w2[j] not in graph[w1[j]]:
            graph[w1[j]].add(w2[j])
            indegree[ord(w2[j]) - ord('a')] += 1
            break

res = topological_sort(graph)
print(res)
