# Leetcode Ques : 206 [Reverse Linked List]

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverse_linkedList(self, head):
        prev = None
        temp = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

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
    lis= LinkedList()
    x = [1,2,3,4,5,6]
    for i in x:
        lis.insert(i)
    print("original:")    
    printList(lis.head)
    new_head = Solution().reverse_linkedList(lis.head)
    print("reversed:")
    printList(new_head)