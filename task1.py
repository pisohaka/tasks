class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        node = self.head
        previous_node = None
        while node is not None:
            if node.value == val:
                if previous_node:
                    previous_node.next = node.next
                else:
                    if not node.next:
                        self.head = node.next
                    else:
                        self.head = node.next
                        self.tail = node.next
                if not all:
                    break
            previous_node = node
            node = node.next

    def clean(self):
        # node = self.head
        # previous_node = None
        # while node is not None:
        #     if previous_node:
        #         del previous_node
        #     if not node.next:
        #         del node
        self.head = None
        self.tail = None

    def find_all(self, val):
        node = self.head
        nodes = []
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if not afterNode:
            newNode.next = self.head
            self.head = newNode
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
            node = node.next

    def to_python_list(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return nodes

def sum_of_lists(firstList: LinkedList, secondList: LinkedList) -> LinkedList:
    resList = LinkedList()
    if firstList.len() == secondList.len():
        list1 = firstList.to_python_list()
        list2 = secondList.to_python_list()
        sum_p_list = [sum(x) for x in zip(list1, list2)]
        for val in sum_p_list:
            resList.add_in_tail(Node(val))
        return resList
