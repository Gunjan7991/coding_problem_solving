# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for double-linked list.
class DoubleListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.prev = prev
        self.val = val
        self.next = next