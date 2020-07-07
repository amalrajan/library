import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def count_occurences(n, d):
    res = 0
    itr = d
    
    while itr <= n:
        if itr % 10 == d:
            res += 1
        elif itr != 0 and itr // 10 == d:
            res += 1
            itr += 1
        elif itr // 10 == d - 1:
            itr += (10 - d)
        else:
            itr += 10
    
    return res


print(count_occurences(11, 1))
