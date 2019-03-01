class Node(object):
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

def reverse(link):
    head = link
    next = link.next
    head.next = None
    while next:
        temp = next.next
        next.next = head
        head = next
        next = temp
    return head

reverse_link = reverse(link)

while reverse_link:
    print(reverse_link.data)
    reverse_link = reverse_link.next

