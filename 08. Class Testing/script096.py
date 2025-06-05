import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add_node(self):
        self.linked_list.add_node(1)
        self.assertEqual(self.linked_list.head.data, 1)

        self.linked_list.add_node(2)
        self.assertEqual(self.linked_list.head.data, 2)

    def test_remove_node(self):
        self.linked_list.add_node(1)
        self.linked_list.add_node(2)
        self.linked_list.add_node(3)

        self.assertEqual(self.linked_list.remove_node(2), True)
        self.assertEqual(self.linked_list.head.next.data, 1)

        self.assertEqual(self.linked_list.remove_node(4), False)

    def test_traverse_list(self):
        self.linked_list.add_node(1)
        self.linked_list.add_node(2)
        self.linked_list.add_node(3)

        self.assertEqual(self.linked_list.traverse_list(), print("3\n2\n1"))


if __name__ == "__main__":
    unittest.main()
