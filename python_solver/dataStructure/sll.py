class SingleListNode:
    """
    Single-LinkedList: In a singly linked list, each node
    has a data element and a reference to the next node.
    The last node's reference points to None (or null),
    indicating the end of the list.
    """

    def __init__(self, node_data, next=None):
        self.node_data = node_data
        self.next = next

    def insertNodeAtTail(head, data):
        mem = head
        new_node = SingleListNode(node_data=data)
        if head == None:
            head = new_node
            mem = head
        else:
            while head.next != None:
                head = head.next
            head.next = new_node
        return mem

    def insertNodeAtHead(head, data):
        new_node = SingleListNode(data)
        if head == None:
            head = new_node
        else:
            new_node.next = head
            head = new_node
        return head

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

    def list_print(head: "SingleListNode"):
        temp = head
        while temp != None:
            if temp.next != None:
                print(temp.val, end="->")
            else:
                print(temp.val)
            temp = temp.next
        print("")
