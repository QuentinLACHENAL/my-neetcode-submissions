# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        Solution.depth = 1
        curNode = root
        Solution.calc(self, curNode, 1)

        return Solution.depth

    def calc(self, curNode, curDepth: int):
        #print(curDepth, Solution.depth)
        if curDepth > Solution.depth:
            Solution.depth += 1
        if curNode.left:
            Solution.calc(self, curNode.left, curDepth + 1)
        if curNode.right:
            Solution.calc(self, curNode.right, curDepth + 1)


        

        