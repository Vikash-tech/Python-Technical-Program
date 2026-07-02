
from collections import deque
# Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Sample Tree (Depth 4)

"""
                1
             /     \
            2       3
          /  \     / \
         4    5   6   7
        / \  / \
       8  9 10 11
"""

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)

# Q1 Traversals

# ---------- Recursive ----------

def preorder_recursive(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder_recursive(root.left)
    preorder_recursive(root.right)


def inorder_recursive(root):
    if not root:
        return
    inorder_recursive(root.left)
    print(root.val, end=" ")
    inorder_recursive(root.right)


def postorder_recursive(root):
    if not root:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root.val, end=" ")

def preorder_iterative(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def inorder_iterative(root):
    stack = []
    current = root

    while stack or current:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        print(current.val, end=" ")

        current = current.right


def postorder_iterative(root):
    if not root:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    print(*result[::-1])


def level_order(root):
    if not root:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

# Q2 Maximum & Minimum Depth

def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root):
    if not root:
        return 0

    if not root.left:
        return 1 + min_depth(root.right)

    if not root.right:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.left), min_depth(root.right))

# Q3 Invert Binary Tree

def invert_tree(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

"""
Before

        4
      /   \
     2     7
    / \   / \
   1  3  6   9

After

        4
      /   \
     7     2
    / \   / \
   9  6  3   1
"""


# Q4 Same Tree & Subtree

def is_same_tree(p, q):

    if not p and not q:
        return True

    if not p or not q:
        return False

    return (
        p.val == q.val
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )


def is_subtree(root, sub):

    if not root:
        return False

    if is_same_tree(root, sub):
        return True

    return is_subtree(root.left, sub) or is_subtree(root.right, sub)

# Q5 Diameter of Binary Tree

def diameter(root):

    ans = 0

    def height(node):
        nonlocal ans

        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        ans = max(ans, left + right)

        return 1 + max(left, right)

    height(root)

    return ans

"""
Why left_height + right_height?

At every node,
Longest path passing through that node

=
height(left subtree)
+
height(right subtree)

Maximum among all nodes is the tree diameter.
"""

# Q6 Zigzag Level Order

def zigzag_level_order(root):

    if not root:
        return []

    result = []
    queue = deque([root])

    left_to_right = True

    while queue:

        level = []

        for _ in range(len(queue)):

            node = queue.popleft()

            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        result.append(level)

        left_to_right = not left_to_right

    return result


# Q7 Build Tree from Preorder & Inorder

def build_tree(preorder, inorder):

    if not preorder or not inorder:
        return None

    index = {v: i for i, v in enumerate(inorder)}

    preorder_index = 0

    def helper(left, right):

        nonlocal preorder_index

        if left > right:
            return None

        root_value = preorder[preorder_index]
        preorder_index += 1

        node = TreeNode(root_value)

        mid = index[root_value]

        node.left = helper(left, mid - 1)
        node.right = helper(mid + 1, right)

        return node

    return helper(0, len(inorder) - 1)

"""
Approach

1. First element of preorder is root.
2. Find root in inorder.
3. Left side -> left subtree.
4. Right side -> right subtree.
5. Repeat recursively.
"""

# Q8 Lowest Common Ancestor

def lowest_common_ancestor(root, p, q):

    if not root:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# LCA in BST

def bst_lca(root, p, q):

    while root:

        if p.val < root.val and q.val < root.val:
            root = root.left

        elif p.val > root.val and q.val > root.val:
            root = root.right

        else:
            return root

"""
Binary Tree:
Search both subtrees.

BST:
Use ordering property.

Both smaller -> Left
Both greater -> Right
Else -> Current node is LCA
"""

if __name__ == "__main__":

    print("=" * 60)
    print("Q1 Traversals")

    print("Preorder Recursive:")
    preorder_recursive(root)
    print()

    print("Preorder Iterative:")
    preorder_iterative(root)
    print()

    print("Inorder Recursive:")
    inorder_recursive(root)
    print()

    print("Inorder Iterative:")
    inorder_iterative(root)
    print()

    print("Postorder Recursive:")
    postorder_recursive(root)
    print()

    print("Postorder Iterative:")
    postorder_iterative(root)

    print("Level Order:")
    level_order(root)
    print()

    print("=" * 60)
    print("Q2 Depth")

    print("Maximum Depth:", max_depth(root))
    print("Minimum Depth:", min_depth(root))

    print("=" * 60)
    print("Q3 Invert Tree")

    invert_tree(root)
    print("Inorder after inversion:")
    inorder_recursive(root)
    print()

    print("=" * 60)
    print("Q5 Diameter")

    print("Diameter:", diameter(root))

    print("=" * 60)
    print("Q6 Zigzag")

    print(zigzag_level_order(root))

    print("=" * 60)
    print("Q7 Build Tree")

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    tree = build_tree(preorder, inorder)

    print("Tree Built Successfully")

    print("=" * 60)
    print("Q8 Lowest Common Ancestor")

    node1 = root.left
    node2 = root.right

    lca = lowest_common_ancestor(root, node1, node2)

    print("LCA:", lca.val)