class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, key):
        if self.head is None:
            self.head = Node(key)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(key)

    def insert_pos(self, key, pos):
        '''
        Indexing starts from 1.
        '''
        if self.head is None or pos == 1:
            self.insert_start(key)
        else:
            prev = self.head
            itr = 1
            while itr < pos - 1 and prev is not None:
                prev = prev.next
                itr += 1

            if prev is None:
                print("Invalid position.")
            elif itr == pos - 1:
                new_node = Node(key)
                new_node.next = prev.next
                prev.next = new_node

    def delete_key(self, key):
        if self.head is None:
            print("List empty.")
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        while curr.key != key and curr is not None:
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def delete_pos(self, pos):
        if self.head is None:
            print("List empty.")
            return
        if pos == 0:
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        itr = 0
        while curr is not None and itr < pos:
            prev = curr
            curr = curr.next
            itr += 1
        if curr is None:
            print("Invalid position")
            return
        elif itr == pos:
            prev.next = curr.next

    def get_length(self):
        length = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            length += 1
        return length

    def get_length_recursive(self, root):
        if root is None:
            return 0
        return 1 + self.get_length_recursive(root.next)

    def get_nth_from_end(self, n):
        '''
        Indexing starts from 1.
        '''
        if self.head is None:
            print("List empty.")
            return
        ref_ptr = self.head
        main_ptr = self.head
        i = 0
        while i < n and ref_ptr is not None:
            ref_ptr = ref_ptr.next
            i += 1
        if ref_ptr is None:
            print("Invalid position")
            return
        while ref_ptr is not None:
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next

        return main_ptr.key

    def get_middle(self):
        if self.head is None:
            print("List empty.")
            return
        ref_ptr = self.head
        main_ptr = self.head

        while ref_ptr and ref_ptr.next:
            ref_ptr = ref_ptr.next.next
            main_ptr = main_ptr.next

        return main_ptr.key

    def detect_loop_hashing(self):
        if self.head is None:
            return
        hashset = set()
        curr = self.head
        while curr:
            if curr in hashset:
                return True
            hashset.add(curr)
            curr = curr.next
        return False

    def detect_loop_floyd(self):
        if self.head is None:
            return
        slow_ptr = self.head
        fast_ptr = self.head

        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
        return False

    def display(self):
        curr = self.head
        while curr:
            print(curr.key, end=' ')
            curr = curr.next
        print()


sll = SingleLinkedList()
sll.insert_start(1)
sll.insert_start(2)
sll.insert_start(3)
sll.insert_end(4)
sll.insert_end(5)
sll.insert_pos(33, 3)

sll.display()

print(sll.get_middle())
