import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_val):
        if not self.head:
            self.head = ListNode(new_val)
            self.tail = self.head
            return

        new_node = ListNode(new_val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

    def get_middle(self, head): 
        if not head:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b): 
        result = None
        
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
            
        # pick either a or b and recur.. 
        if a.val <= b.val: 
            result = a 
            result.next = self.sorted_merge(a.next, b) 
        else: 
            result = b 
            result.next = self.sorted_merge(a, b.next) 
        return result 

    def merge_sort(self, h):
        if not h or not h.next:
            return h

        middle = self.get_middle(h) 
        nexttomiddle = middle.next
        middle.next = None
        left = self.merge_sort(h) 
        right = self.merge_sort(nexttomiddle) 
        sortedlist = self.sorted_merge(left, right) 
        return sortedlist 
        


sll = LinkedList()
sll.append(1)
sll.append(5)
sll.append(3)
sll.append(7)
sll.append(2)

sll.display()

sll.merge_sort(sll.head)
sll.display()
