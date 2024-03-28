from typing import List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)

# Test the solution
def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.left, level + 1)

# Example usage:
# Create a sorted array
sorted_array = [-10,-3,0,5,9]
# Convert the sorted array to a BST
bst_root = Solution().sortedArrayToBST(sorted_array)
# Print the BST
printTree(bst_root)

