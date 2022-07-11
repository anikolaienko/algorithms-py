from unittest import TestCase
from algorithms.binary_tree.traversals import Node, in_order, pre_order, post_order

class InOrderTest(TestCase):
    def setUp(self) -> None:
        self.root = Node(10) \
            .insert(5) \
            .insert(2) \
            .insert(1) \
            .insert(5) \
            .insert(15) \
            .insert(13) \
            .insert(12) \
            .insert(14) \
            .insert(22)
        
    def tearDown(self) -> None:
        self.root = None

    def test_in_order__success(self):
        expected = [1, 2, 5, 5, 10, 12, 13, 14, 15, 22]

        assert expected == in_order(self.root)

    def test_pre_order__success(self):
        expected = [10, 5, 2, 1, 5, 15, 13, 12, 14, 22]

        assert expected == pre_order(self.root)

    def test_post_order__success(self):
        expected = [1, 2, 5, 5, 12, 14, 13, 22, 15, 10]

        assert expected == post_order(self.root)