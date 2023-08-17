class SingleListNode:
    """
    Single-LinkedList: In a singly linked list, each node
    has a data element and a reference to the next node.
    The last node's reference points to None (or null),
    indicating the end of the list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_queue(lst: list[any]) -> "SingleListNode":
        """
        queue type insertion where data are added in bottom,
        insertion order is kept:
        insert(1)
        insert(2)
        insert(3)

        head->1->2->3
        """
        head, curr = None, None
        for val in lst:
            temp = SingleListNode(val, next=None)
            if head == None:
                head = temp
                curr = head
            else:
                curr.next = temp
        return head

    def list_stack(lst: list[any]) -> "SingleListNode":
        """
        stack type insertion where new data gets added to top,
        insertion order are reversed:
        insert(1)
        insert(2)
        insert(3)

        head->3 -> 2 -> 1
        """
        head = None
        for val in lst:
            head = SingleListNode(val, next=head)
        return head

    def list_print(head: 'SingleListNode'):
        temp = head
        while temp != None:
            if temp.next != None:
                print(temp.val, end="->")
            else:
                print(temp.val)
            temp = temp.next
        print("")
