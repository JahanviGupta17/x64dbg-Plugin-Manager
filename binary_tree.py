class Node:
    def __init__(self, key):
        """
        Create a new node with the given key.

        Args:
            key: The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def insert(self, root, key):
        """
        Insert a new node with the given key into the binary tree.

        Args:
            root: The current root node of the tree.
            key: The value to be inserted.

        Returns:
            The updated tree with the new node.
        """
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    
    for key in keys:
        root = tree.insert(root, key)
