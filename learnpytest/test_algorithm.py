import sorting
import pytest

from sorting import *


@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 5, 3, 8, 6]


def test_bubble_sort(unsorted_list):
    s1 = bubble_sort(unsorted_list)
    assert s1 == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_sort(unsorted_list):
    s1 = selection_sort(unsorted_list)
    assert s1 == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_insertion_sort(unsorted_list):
    s1 = insertion_sort(unsorted_list)
    assert unsorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_sort(unsorted_list):
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list
