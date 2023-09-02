class Solution:
    def add_two_numbers(l1, l2):
        result = curr = ListNode(0)
        cursum = 0
        while l1 or l2:
            if l1:
                cursum += l1.val
                l1 = l1.next
            if l2:
                cursum += l2.val
                l2 = l2.next

            curr.next = ListNode(cursum % 10)
            curr = curr.next
            cursum = cursum // 10
        
        if cursum != 0:
            curr.next = ListNode(cursum)
        return result.next
     
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) :
        self.head = None

    def insert(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

def printList( head):
    temp = head
    while(temp):
        print(temp.val, end=" ")
        temp = temp.next
    print()
      
if __name__ == "__main__":
    lis1= LinkedList()
    lis2 = LinkedList()
    x = [3,4,2]
    y = [4,6,5]
    for i in x:
        lis1.insert(i)
    for i in y:
        lis2.insert(i)

    c = Solution.add_two_numbers(lis1.head, lis2.head)
    printList(c)
