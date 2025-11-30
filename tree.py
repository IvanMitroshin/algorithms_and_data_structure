from collections import deque
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert(node.right, key)

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)


    def bfs(self):
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.key, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')