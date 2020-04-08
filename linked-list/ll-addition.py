class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, arr=None):
        self.head = None

        if arr:
            curr = None
            for elem in arr:
                if self.head is None:
                    self.head = Node(elem)
                    curr = self.head
                else:
                    curr.next = Node(elem)
                    curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next


def add_numbers(l1, l2):
    l1, l2 = l1.head, l2.head
    res = LinkedList()
    res.head = Node(None)
    curr = res.head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry, out = divmod(val1+val2+carry, 10)
        
        curr.next = Node(out)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    res.head = res.head.next
    return res


def subtract_numbers(l1, l2):
    l1, l2 = l1.head, l2.head
    res = LinkedList()
    res.head = Node(None)
    curr = res.head

    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        if val1 >= val2:
            out = val1 - val2
        else:
            


l1 = LinkedList([1, 2, 3])
l2 = LinkedList([1, 2, 9])

res = add_numbers(l1, l2)
res.display()
