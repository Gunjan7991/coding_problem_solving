from codding.medianOfTwoSortedArray import (
    findMedianSortedArrays,
    findMedianSortedArraysFast,
)


def test_findMedianSortedArrays_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.00000


def test_findMedianSortedArrays_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.50000


def test_findMedianSortedArrays_3():
    assert findMedianSortedArrays([1, 2, 3], [4, 5, 6]) == 3.50000


def test_findMedianSortedArrays_4():
    assert findMedianSortedArrays([5, 6, 7], [9]) == 6.50000


def test_findMedianSortedArrays_5():
    assert findMedianSortedArrays([1], [1]) == 1.00000


def test_findMedianSortedArraysFast_1():
    assert findMedianSortedArraysFast([1, 3], [2]) == 2.00000


def test_findMedianSortedArraysFast_2():
    assert findMedianSortedArraysFast([1, 2], [3, 4]) == 2.50000


def test_findMedianSortedArraysFast_3():
    assert findMedianSortedArraysFast([1, 2, 3], [4, 5, 6]) == 3.50000


def test_findMedianSortedArraysFast_4():
    assert findMedianSortedArraysFast([5, 6, 7], [9]) == 6.50000


def test_findMedianSortedArraysFast_5():
    assert findMedianSortedArraysFast([1], [1]) == 1.00000
