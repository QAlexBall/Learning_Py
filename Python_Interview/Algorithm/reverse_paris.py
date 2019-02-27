class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @staticmethod
    def static_swap_paris(head):
        if head != None and head.next != None:
            next = head.next
            head.next = Solution.static_swap_paris(next.next)
            next.next = head
            return next
        return head

def output(l):
    for i in range(5):
        print(l.val)
        l = l.next

head = ListNode(0)
l = head
for i in range(1, 5):
    head.next = ListNode(i)
    head = head.next
result = l.next

Solution.static_swap_paris(l)
output(result)



ceh