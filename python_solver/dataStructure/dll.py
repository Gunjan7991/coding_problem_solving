class DoubleListNode:
    """
    Double_LinkedList: In a doubly linked list, each node has a
    data element, a reference to the next node, and a reference
    to the previous node. This allows for traversal in both
    directions.
    """

    def __init__(self, val: any, next=None, prev=None):
        self.prev = prev
        self.val = val
        self.next = next

    def list_append(lst: list[any]) -> ["DoubleListNode", "DoubleListNode"]:
        """
        queue type insertion where data are added in bottom,
        insertion order is kept:
        insert(1)
        insert(2)
        insert(3)
        head->1<->2<->3<-tail

        returns list: [head, tail]
        """
        head, tail = None, None
        for val in lst:
            temp = DoubleListNode(val, next=None, prev=None)
            if head == None and tail == None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                temp.prev = tail
                tail = temp
        return [head, tail]

    def list_stack(lst: list(any)) -> list["DoubleListNode", "DoubleListNode"]:
        """
        stack type insertion where new data gets added to top,
        insertion order are reversed:
        insert(1)
        insert(2)
        insert(3)
        tail->1<->2<->3<-head

        returns list: [head, tail]
        """
        head, tail = DoubleListNode.list_append(lst)
        return [tail, head]

    def list_print_head(head: "DoubleListNode"):
        temp = head
        while temp != None:
            if temp.next != None:
                print(temp.val, end="->")
            else:
                print(temp.val)
            temp = temp.next
        print("")

    def list_print_tail(tail: "DoubleListNode"):
        temp = tail
        while temp != None:
            if temp.prev != None:
                print(temp.val, end="<-")
            else:
                print(temp.val)
            temp = temp.prev
        print("")
