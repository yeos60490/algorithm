# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                answer = [root.val] + answer #거꾸로 넣기
                root = root.right #preorder 와 반대 순 
                
            else:
                pre = stack.pop()
                root = pre.left
            
        return answer
