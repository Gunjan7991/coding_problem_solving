from  typing import Optional
class SingleListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_convert(lst: list[any]) -> "SingleListNode":
        """
        Appends the values in the fron and converts the given list to LinkedList in reverse order.
        """
        head = None
        for val in lst:
            head = SingleListNode(val, next=head)
        return head
    
    def list_convert2(lst: list[any]) -> Optional["SingleListNode"]:
        """
        Appends the values in the back and converts the given list to LinkedList as it is.
        """
        head = SingleListNode()
        temp = head
        for val in lst:
            temp.next = SingleListNode(val)
            temp = temp.next
        
        return head.next

    def list_print(linkedList: "SingleListNode") -> None:
        while linkedList:
            if not linkedList:
                print(linkedList.val, end="->")
            else:
                print(linkedList.val)
            linkedList = linkedList.next
        return None
