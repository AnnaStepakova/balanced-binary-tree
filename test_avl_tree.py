from unittest import TestCase
from avl_tree import AVLTree


class TestAVLTreeRotations(TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_left_left(self):
        self.tree.insert_list([(24, 0), (20, 11), (26, 1), (15, 1), (22, 1), (14, 0)])
        self.assertEqual(self.tree._root.key, 20)
        self.assertEqual(self.tree._root.right.key, 24)
        self.assertEqual(self.tree._root.left.key, 15)

    def test_left_right(self):
        self.tree.insert_list([(15, 0), (10, 1), (9, 1), (11, 0), (23, 0), (13, 0)])
        self.assertEqual(self.tree._root.key, 11)
        self.assertEqual(self.tree._root.right.key, 15)
        self.assertEqual(self.tree._root.left.key, 10)

    def test_right_right(self):
        self.tree.insert_list([(10, 1), (5, 1), (12, 1), (11, 1), (13, 1), (15, 1)])
        self.assertEqual(self.tree._root.key, 12)
        self.assertEqual(self.tree._root.right.key, 13)
        self.assertEqual(self.tree._root.left.key, 10)

    def test_right_left(self):
        self.tree.insert_list([(10, 1), (5, 1), (20, 2), (21, 22), (15, 3), (11, 2), (17, 3)])
        self.assertEqual(self.tree._root.key, 15)
        self.assertEqual(self.tree._root.right.key, 20)
        self.assertEqual(self.tree._root.left.key, 10)


class TestAVLTreeMethods(TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.tree.insert_list([(10, 0), (5, 1), (15, 2), (20, 0), (1, 1), (12, 1)])
        self.tree.insert(7)

    def test_delete(self):
        self.tree.delete(10)
        self.assertEqual(self.tree._root.key, 12)

    def test_contains(self):
        self.assertEqual(15 in self.tree, True)
        self.assertEqual(2 in self.tree, False)

    def test_getitem_and_setitem(self):
        self.assertEqual(self.tree[5], 1)
        self.tree[5] = 100
        self.assertEqual(self.tree[5], 100)
        self.assertEqual(self.tree[155], None)
        self.tree[155] = 10
        self.assertEqual(self.tree[155], 10)
