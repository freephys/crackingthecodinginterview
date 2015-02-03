import unittest

from problem6 import next_node
from problem3 import create_bst


class Visitor(object):

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            self.visit(node)
            self.in_order(node.right)

    def visit(self, node):
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node


class TestNextNode(unittest.TestCase):

    def setUp(self):
        self.tree = create_bst(range(7))

        visitor = Visitor()
        visitor.in_order(self.tree.root)
        self.tree.root.parent = None

    def test_complete(self):
        node = self.tree.root.left.left
        self.assertEquals(node.left, None)
        self.assertEquals(node.right, None)
        self.assertEquals(node.value, 0)

        node = next_node(node)
        self.assertEquals(node.value, 1)

        node = next_node(node)
        self.assertEquals(node.value, 2)

        node = next_node(node)
        self.assertEquals(node.value, 3)

        node = next_node(node)
        self.assertEquals(node.value, 4)

        node = next_node(node)
        self.assertEquals(node.value, 5)

        node = next_node(node)
        self.assertEquals(node.value, 6)
