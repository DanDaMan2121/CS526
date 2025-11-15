import random

# ===============================
# Node ADT
# ===============================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


# ===============================
# Binary Search Tree ADT
# ===============================
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ---------------------------
    # Add Node
    # ---------------------------
    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)
        # Ignore duplicates

    # ---------------------------
    # Find Node
    # ---------------------------
    def find_node(self, value):
        return self._find(self.root, value)

    def _find(self, current, value):
        if current is None:
            return None
        if value == current.value:
            return current
        elif value < current.value:
            return self._find(current.left, value)
        else:
            return self._find(current.right, value)

    # ---------------------------
    # Delete Node
    # ---------------------------
    def delete_node(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            # Case 1: no children
            if current.left is None and current.right is None:
                return None
            # Case 2: one child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Case 3: two children
            min_larger_node = self._find_min(current.right)
            current.value = min_larger_node.value
            current.right = self._delete(current.right, min_larger_node.value)

        return current

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ---------------------------
    # Print Tree (in-order traversal)
    # ---------------------------
    def print_tree(self):
        print("Tree (In-Order): ", end="")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


# ===============================
# Demonstration
# ===============================
def main():
    bst = BinarySearchTree()

    # Generate random input
    size = random.randint(5, 50)
    input_values = random.sample(range(1, 1001), size)

    print("Random Input Set (size =", size, "):")
    print(input_values)

    # Build initial tree
    for v in input_values:
        bst.add_node(v)

    print("\nInitial Tree:")
    bst.print_tree()

    # Add a random node (not already in tree)
    new_value = random.choice([v for v in range(1, 1001) if v not in input_values])
    print(f"\nAdding node: {new_value}")
    bst.add_node(new_value)
    bst.print_tree()

    # Delete a random node from the tree
    del_value = random.choice(input_values)
    print(f"\nDeleting node: {del_value}")
    bst.delete_node(del_value)
    bst.print_tree()

    # Test find_node (positive case)
    find_val = random.choice(input_values)
    found = bst.find_node(find_val)
    print(f"\nSearching for existing node {find_val}: {'Found' if found else 'Not Found'}")

    # Test find_node (negative case)
    not_in_tree = random.choice([v for v in range(1, 1001) if v not in input_values])
    found = bst.find_node(not_in_tree)
    print(f"Searching for missing node {not_in_tree}: {'Found' if found else 'Not Found'}")


main()