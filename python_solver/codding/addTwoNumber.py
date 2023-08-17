from typing import Optional
from linkedList import ListNode

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    while l1.next == None:
        print(l1.val)
        l1 = l1.next
    print(l1.val)
    

