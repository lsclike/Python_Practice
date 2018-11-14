class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

    def insert_real(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def has_cycle(head):
    if head is None:
        return False

    p1 = head
    p2 = head

    while not (p1 is None or p2.next.next is None):
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True

    return False


if __name__ == '__main__':
    test = SinglyLinkedList()
    n1 = SinglyLinkedListNode('n1')
    n2 = SinglyLinkedListNode('n2')
    n3 = SinglyLinkedListNode('n3')
    test.insert_node('test')
    test.insert_real(n1)
    test.insert_real(n2)
    test.insert_real(n3)
    test.insert_real(n2)
    result = has_cycle(test.head)
    print(result)
    # while test.head:
    #     print(test.head.data, end=' ')
    #     test.head = test.head.next
