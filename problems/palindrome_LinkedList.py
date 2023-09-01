# Leetcode Ques : 234 [Palindrome Linked List]

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def palindrome_linkedList(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)
        fast = head

        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse(self, node):
        prev = None
        temp = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
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
      
if __name__ == "__main__":
    a= LinkedList()
    a.insert(1)
    a.insert(2)
    a.insert(2)
    a.insert(1)
    if Solution().palindrome_linkedList(a.head):
        print("Yes")
    else:
        print("No")