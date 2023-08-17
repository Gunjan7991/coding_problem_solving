from codding.addTwoNumber import addTwoNumbers
from codding.mylist import SingleListNode


def compare_linkedList(l1, l2) -> bool:
    while l1 != None or l2 != None:
        v1, v2 = 0, 0
        if l1 != None:
            v1 = l1.val
            l1 = l1.next

        if l2 != None:
            v2 = l2.val
            l2 = l2.next
        if v1 != v2:
            print(v1, v2)
            return False
    return True


def test_addTwoNumbers_1():
    l1 = SingleListNode.list_convert([2, 4, 3])
    l2 = SingleListNode.list_convert([5, 6, 4])
    assert compare_linkedList(
        addTwoNumbers(l1, l2), SingleListNode.list_convert([8, 0, 7])
    )


def test_addTwoNumbers_2():
    l1 = SingleListNode.list_convert([0])
    l2 = SingleListNode.list_convert([0])
    assert compare_linkedList(addTwoNumbers(l1, l2), SingleListNode.list_convert([0]))


def test_addTwoNumbers_3():
    l1 = SingleListNode.list_convert([9, 9, 9, 9, 9, 9, 9])
    l2 = SingleListNode.list_convert([9, 9, 9, 9])
    assert compare_linkedList(
        addTwoNumbers(l1, l2), SingleListNode.list_convert([1, 0, 0, 0, 9, 9, 9, 8])
    )


def test_addTwoNumbers_4():
    l1 = SingleListNode.list_convert([0])
    l2 = SingleListNode.list_convert([2, 7, 8])
    assert compare_linkedList(
        addTwoNumbers(l1, l2), SingleListNode.list_convert([2, 7, 8])
    )


def test_addTwoNumbers_5():
    l1 = SingleListNode.list_convert([1, 6, 9, 5, 6, 1, 4, 8, 6, 7])
    l2 = SingleListNode.list_convert([1, 0, 5, 6, 5, 9, 1, 9, 4, 6])
    assert compare_linkedList(
        addTwoNumbers(l1, l2),
        SingleListNode.list_convert([2, 7, 5, 2, 2, 0, 6, 8, 1, 3]),
    )
