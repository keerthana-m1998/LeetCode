# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inOrder=[]
        def inOrderTraversal(node):
            if not node:
                return
            inOrderTraversal(node.left)
            inOrder.append(node.val)
            inOrderTraversal(node.right)
        inOrderTraversal(root)

        left,right=0,len(inOrder)-1
        while left<right:
            summ = inOrder[left]+inOrder[right]
            if summ==k:
                return True
            elif summ<k:
                left+=1
            else:
                right-=1
        return False
