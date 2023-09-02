# Leetcode Ques : 160 [Intersection of Two nodes]

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

class Solution:
    def intersection_node(self, headA, headB):
        cur1 = headA
        cur2 = headB
        if cur1 == None or cur2 == None:
            return
        
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

            if cur1 == cur2:
                return cur1
            if cur1 == None:
                cur1 = headB
            if cur2 == None:
                cur2 = headA
        return cur1

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
    x = [4,1,8,4,5]
    y = [5,6,1,8,4,5]
    for i in x:
        lis1.insert(i)
    for i in y:
        lis2.insert(i)
    Solution().intersection_node(lis1.head, lis2.head)
    
    
