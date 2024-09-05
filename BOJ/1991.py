import sys
sys.stdin=open("./boj/test_case.txt","r")
input=sys.stdin.readline

n = int(input().strip())

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, child_node, child):
        if child == "left":
            node.left = child_node
        else:
            node.right = child_node
        return node

    def traverseInorder(self, node):
        if node:
            self.traverseInorder(node.left)
            print(node.data, end="")
            self.traverseInorder(node.right)
    
    def traversePreorder(self, node):
        if node:
            print(node.data, end="")
            self.traversePreorder(node.left)
            self.traversePreorder(node.right)
    
    def traversePostorder(self, node):
        if node:
            self.traversePostorder(node.left)
            self.traversePostorder(node.right)
            print(node.data, end="")


tree = Tree()
root = tree.createNode("A")
nodes = [root]
for _ in range(n):
    parent, left_child, right_child = input().strip().split()
    for node in nodes:
        if node.data == parent:
            parent_node = node

    if left_child != ".":
        left_node = Node(left_child)
        nodes.append(left_node)
        tree.insert(parent_node, left_node, "left")
    if right_child != ".":
        right_node = Node(right_child)
        nodes.append(right_node)
        tree.insert(parent_node, right_node, "right")

tree.traversePreorder(root)
print(" ")
tree.traverseInorder(root)
print(" ")
tree.traversePostorder(root)