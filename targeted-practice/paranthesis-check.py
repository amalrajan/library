import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def solve(s):
    n = len(s)
    stack = []

    d = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in range(n):
        if s[i] in '{([':
            stack.append(s[i])
        elif  stack and stack[-1] == d[s[i]]:
            stack.pop()
        else:
            return False
        
    return not stack

for tc in range(int(input())):
    s = input()
    res = solve(s)

    print('balanced' if res else 'unbalanced')
