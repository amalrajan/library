import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass

def is_safe(u, pos, path):
    if graph[path[pos - 1]][u] == 0:
        return False
    
    if u in path:
        return False
    
    return True

def ham_cycle():
    path = [-1] * (v)
    path[0] = 0

    if not ham_cycle_util(path, 1):
        print("Solution does not exist")
        return
    
    print(path + [path[0]])
    return True

def ham_cycle_util(path, pos):
    if pos == v:
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    
    for u in range(1, v):
        if is_safe(u, pos, path):
            path[pos] = u

            if ham_cycle_util(path, pos + 1):
                return True
            
            path[pos] = -1
    
    return False


graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

v = 5

ham_cycle()
