class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def inorderTraversal_recursive(self, root):
        result = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result

    def inorderTraversal_iterative(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    sol = Solution()

    print("Recursive:", sol.inorderTraversal_recursive(root))
    print("Iterative:", sol.inorderTraversal_iterative(root))