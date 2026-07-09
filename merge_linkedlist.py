class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(9)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)
head2.next.next.next.next = Node(10)

dummy = Node(0)
tail = dummy
