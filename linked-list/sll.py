import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def insert_pos(self, val, pos):
        # Indexing starts from 1
        if not self.head or pos == 1:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            ptr = 1

            while ptr < pos - 1 and curr:
                curr = curr.next
                ptr += 1

            if not curr:
                print('Index out of bounds')
                return
            
            new_node = Node(val, next=curr.next)
            curr.next = new_node

    def delete_key(self, key):
        curr = self.head
        prev = None
        
        if curr.val == key:
            self.head = self.head.next
            return

        while curr and curr.val != key:
            prev = curr
            curr = curr.next
        prev.next = curr.next


    def delete_pos(self, pos):
        curr = self.head
        if pos == 1:
            self.head = self.head.next
            return
        
        ptr = 1
        while curr and ptr < pos - 1:
            curr = curr.next
            ptr += 1
        curr.next = curr.next.next

    def get_length(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        return length

    def get_length_recursive(self, root):
        if not root:
            return 0
        return 1 + self.get_length_recursive(root.next)

    def n_th_from_end(self, n):
        if not self.head:
            return None
        
        refptr = self.head
        mainptr = self.head
        
        for i in range(n):
            if refptr:
                refptr = refptr.next
            else:
                print('Index out of bounds')
                return
        
        while refptr:
            mainptr = mainptr.next
            refptr = refptr.next
        
        return mainptr.val

    def get_middle(self):
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val

    def detect_loop_hashing(self):
        hset = set()
        curr = self.head

        while curr:
            if curr.val in hset:
                return True
            hset.add(curr.val)
            curr = curr.next

        if not curr:
            return False

    def detect_loop_floyd(self):
        if not self.head:
            return

        slow = self.head
        fast = self.head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()


sll = SingleLinkedList()
sll.insert_start(1)
sll.insert_start(2)
sll.insert_start(3)

sll.display()

sll.insert_end(4)
sll.insert_end(5)

sll.display()

sll.delete_pos(5)
sll.display()

print(sll.n_th_from_end(4))
print(sll.get_middle())
print(sll.detect_loop_hashing())