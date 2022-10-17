class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


list_1 = LinkedList()
node_1 = Node(8)
node_2 = Node(5)
node_3 = Node(7)

list_1.head = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_2

slow_pointer = node_1
fast_pointer = node_1.next

while fast_pointer is not None and fast_pointer != slow_pointer:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
if fast_pointer is None:
    print("Loop is not present")
else:
    print("Loop is present")
