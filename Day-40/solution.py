class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):

        def validate(node, low=float('-inf'), high=float('inf')):

            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root)


if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    solution = Solution()
    print("Is valid BST:", solution.isValidBST(root))