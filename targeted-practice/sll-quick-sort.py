import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_list(arr):
    head = Node(None)
    curr = head

    for elem in arr:
        curr.next = Node(elem)
        curr = curr.next

    return (head.next, curr)


def display(root):
    while root:
        print(root.val, end=' ')
        root = root.next
    print()


def partition(start, end):
    if start == end or not start or not end:
        return start

    pivot_prev = start
    curr = start
    pivot = end.val

    while start != end:
        if start.val < pivot:
            pivot_prev = curr
            curr.val, start.val = start.val, curr.val
            curr = curr.next

        start = start.next

    curr.val, pivot = pivot, curr.val
    return pivot_prevz


def quick_sort(start, end):
    if start == end:
        return

    pivot_prev = partition(start, end)
    quick_sort(start, pivot_prev)

    if pivot_prev and pivot_prev == start:
        quick_sort(pivot_prev.next, end)
    elif pivot_prev and pivot_prev.next:
        quick_sort(pivot_prev.next, end)


root, tail = build_list([4, 2, 3, 4, 5])
display(root)

quick_sort(root, tail)
display(root)
