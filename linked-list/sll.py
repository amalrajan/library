import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            temp = ListNode(val)
            temp.next = self.head
            self.head = temp

    def insert_end(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)

    def insert_pos(self, val, pos):
        if not self.head or pos == 0:
            self.insert_start(val)
        else:
            pos -= 1
            temp = self.head
            for i in range(pos):
                if not temp.next:
                    return
                temp = temp.next

            new_node = ListNode(val)
            new_node.next = temp.next
            temp.next = new_node

    def delete_key(self, key):
        if self.head.val == key:
            self.head = self.head.next

        curr = self.head.next
        prev = self.head
        while curr:
            if curr.val == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next

    def delete_pos(self, pos):
        if pos == 0:
            self.head = self.head.next

        prev = self.head
        curr = self.head.next

        for i in range(1, pos):
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

    def get_length(self):
        length = 0
        curr = self.head
        while curr:
            curr = curr.next
            length += 1

        return length

    def get_length_recursive(self, node):
        if node:
            return 1 + self.get_length_recursive(node.next)
        return 0

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next


sll = SinglyLinkedList()
