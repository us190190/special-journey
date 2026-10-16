# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.result = []

        def _get_height(r: Optional[TreeNode]) -> int:
            if not r:
                return -1
            
            left = _get_height(r.left)
            right = _get_height(r.right)

            c_height = max(left, right) + 1
            
            if len(self.result) == c_height:
                self.result.append([])

            self.result[c_height].append(r.val)
            return c_height
        
        _get_height(root)

        return self.result



        