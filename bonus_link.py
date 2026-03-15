
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


nums = [2,4,3]

l2 = ListNode(3, None)
l1 = ListNode(4, l2)
head = ListNode(2, l1)

start = head
while start != None:
    print(start.val)
    start = start.next
