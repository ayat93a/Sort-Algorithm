from insertion_sort import Insertion_Sort


def test_Insertion_Sort1():
    assert Insertion_Sort.insertionSort([0,1,5,9,2,3]) == [0,1,2,3,5,9]


def test_Insertion_Sort2():
    assert Insertion_Sort.insertionSort([0,-1,5,-9,2,3]) == [-9,-1,0,2,3,5]