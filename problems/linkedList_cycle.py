# Leetcode Ques : 141 [Linked List Cycle]

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

def linkedList_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        if fast.next == slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
