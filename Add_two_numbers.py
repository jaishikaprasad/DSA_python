class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

def add_two_numbers(l1, l2):
    result = current = ListNode()
    cursum = 0

    while l1 or l2:
        if l1:
            cursum += l1.val
            l1 = l1.next
        if l2:
            cursum += l2.val
            l2 = l2.next

        current.next = ListNode(cursum % 10)
        current = current.next
        cursum = cursum // 10

    if cursum != 0:
        current.next = ListNode(cursum)

    return result.next
    
l1 = [2,4,3]
l2 = [5,6,4]
print(add_two_numbers(l1, l2))
