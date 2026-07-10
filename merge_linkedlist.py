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

def merge(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

result = merge(head1, head2)
printlist(result)