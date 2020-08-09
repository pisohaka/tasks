import pytest
from task1 import LinkedList, Node


@pytest.mark.parametrize("input_val, expected", [([1], []), ([], []), ([2, 1, 3], [2, 3]), ([1, 1, 1], [1, 1])])
def test_delete(input_val, expected):
    s_list = LinkedList()
    for val in input_val:
        s_list.add_in_tail(Node(val))
    s_list.delete(1)
    assert s_list.to_python_list() == expected

@pytest.mark.parametrize("input_val, expected", [([1], []), ([1,1,1], []), ([1, 2, 1, 3, 1], [2, 3])])
def test_delete_all(input_val, expected):
    s_list = LinkedList()
    for val in input_val:
        s_list.add_in_tail(Node(val))
    s_list.delete(1, all=True)
    assert s_list.to_python_list() == expected

@pytest.mark.parametrize("input_val, expected", [([1], []), ([], []), ([1, 2, 1, 3, 1], [])])
def test_clean(input_val, expected):
    s_list = LinkedList()
    for val in input_val:
        s_list.add_in_tail(Node(val))
    s_list.clean()
    assert s_list.to_python_list() == expected

@pytest.mark.parametrize("input_val, expected", [([1], [1]), ([], []), ([1, 2, 1, 3, 1], [1, 1, 1])])
def test_find_all(input_val, expected):
    s_list = LinkedList()
    for val in input_val:
        s_list.add_in_tail(Node(val))
    result = []
    for node in s_list.find_all(1):
        result.append(node.value)
    assert result == expected

@pytest.mark.parametrize("input_val, expected", [([1], 1), ([], 0), ([1, 2, 1, 3, 1], 5)])
def test_len(input_val, expected):
    s_list = LinkedList()
    for val in input_val:
        s_list.add_in_tail(Node(val))
    assert s_list.len() == expected

# @pytest.mark.parametrize("input_val, expected", [([1], [1, 2]), ([], []), ([1, 2, 1, 3, 1], [1, 1, 1])])
# def test_insert(input_val, expected):
#     s_list = LinkedList()
#     for val in input_val:
#         s_list.add_in_tail(Node(val))
#     s_list.insert()
#     assert result == expected
