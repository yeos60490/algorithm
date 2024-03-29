# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        stack = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                pre = stack.pop()
                answer.append(pre.val) #inorder는 여기서 출력 
                root = pre.right
                
                
        return answer
