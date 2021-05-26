import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def prec(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    
    return -1

def infix_to_postfix(inf):
    stack = []
    post = ''

    for ch in inf:
        if ch.isalpha():
            post += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                post += stack.pop()
            if stack[-1] == '(':
                stack.pop()
        else:
            while stack and prec(ch) <= prec(stack[-1]):
                post += stack.pop()
            stack.append(ch)

    while stack:
        post += stack.pop()

    return post

for _ in range(int(input())):
    inf = input()
    print(infix_to_postfix(inf))
