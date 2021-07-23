# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []

        stack = []
        while root or stack:
            if root:
                stack.append(root)
                answer.append(root.val) #preorder 는 먼저 출력 
                root = root.left
    
            else:
                pre = stack.pop() #inorder는 여기서 출력
                root = pre.right
                
        '''   
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        '''
                
        return answer
