from leetcode.mergeTwoLists import mergeTwoLists
from dataStructure.mylist import SingleListNode


def compare_linkedList(l1, l2) -> bool:
    if not l1 and not l2:
        return True
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


def test_mergeTwoLists_1():
    l1 = SingleListNode.list_convert2([1, 2, 4])
    l2 = SingleListNode.list_convert2([1, 3, 4])
    l3 = SingleListNode.list_convert2([1, 1, 2, 3, 4, 4])
    assert compare_linkedList(mergeTwoLists(l1, l2), l3) == True


def test_mergeTwoLists_2():
    l1 = SingleListNode.list_convert2([])
    l2 = SingleListNode.list_convert2([])
    l3 = SingleListNode.list_convert2([])
    assert compare_linkedList(mergeTwoLists(l1, l2), l3) == True


def test_mergeTwoLists_3():
    l1 = SingleListNode.list_convert2([])
    l2 = SingleListNode.list_convert2([0])
    l3 = SingleListNode.list_convert2([0])
    assert compare_linkedList(mergeTwoLists(l1, l2), l3) == True


def test_mergeTwoLists_4():
    l1 = SingleListNode.list_convert2([-2, -1])
    l2 = SingleListNode.list_convert2([0, 1, 2])
    l3 = SingleListNode.list_convert2([-2, -1, 0, 1, 2])
    assert compare_linkedList(mergeTwoLists(l1, l2), l3) == True


def test_mergeTwoLists_5():
    l1 = SingleListNode.list_convert2([1])
    l2 = SingleListNode.list_convert2([])
    l3 = SingleListNode.list_convert2([1])
    assert compare_linkedList(mergeTwoLists(l1, l2), l3) == True
