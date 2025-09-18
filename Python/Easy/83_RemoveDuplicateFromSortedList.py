class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def deleteDuplicates(head):
        current = head
        while current:
            if current.next != None and current.val == current.next.val:
                prev = current
                current.next = current.next.next
            else:
                current = current.next
        
        return head

node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(2)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

deleteDuplicates(node1)