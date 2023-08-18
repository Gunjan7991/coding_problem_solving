from typing import Optional
from dataStructure.mylist import SingleListNode


def addTwoNumbers(
    l1: Optional[SingleListNode], l2: Optional[SingleListNode]
) -> Optional[SingleListNode]:
    v1: str = ""
    v2: str = ""
    while l1 != None or l2 != None:
        if l1 != None:
            v1 += str(l1.val)
            l1 = l1.next

        if l2 != None:
            v2 += str(l2.val)
            l2 = l2.next
    v1, v2 = v1[::-1], v2[::-1]
    value = int(v1) + int(v2)
    prev = None
    for i in str(value):
        prev = SingleListNode(int(i), prev)
    return prev
