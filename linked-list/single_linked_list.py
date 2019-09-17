class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, arr):
        prev = None
        for elem in arr:
            node = Node(elem)
            if self.head is None:
                self.head = node
                prev = self.head
            else:
                prev.next = node
                prev = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def delete_node(self, data):
        temp = self.head
        if temp.data == data:
            # Head case
            temp.data = None
            self.head = temp.next
            temp = temp.next

        prev = self.head
        while temp:
            if temp.data == data:
                temp.data = None
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next

    def modify_node(self, data, new_data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.data = new_data
            temp = temp.next


ll = LinkedList()
ll.create_list([1, 2, 3, 4, 5])

ll.display()

ll.modify_node(1, 11)

ll.display()
