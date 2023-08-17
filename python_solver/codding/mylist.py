class SingleListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_convert(lst: list[any]) -> "SingleListNode":
        head = None
        for val in lst:
            head = SingleListNode(val, next=head)
        return head

    def list_print(linkedList: "SingleListNode") -> None:
        while linkedList != None:
            if linkedList.next != None:
                print(linkedList.val, end="->")
            print(linkedList.val)
            linkedList = linkedList.next
