# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        root = self.buildTree( preorder, postorder)
        return root

    def buildTree(self, preorder, postorder):
          if len(preorder)==0 or len(postorder) == 0:
              return None
          elif len(preorder) == 1 and len(postorder)==1:
              root = TreeNode(preorder[0])
              return root
          elif len(preorder) == 2 and len(postorder)==2:
              root = TreeNode(preorder[0])
              root.left = TreeNode(preorder[-1])
              root.right = None
              return root
          elif len(preorder) > 2 and len(postorder)> 2:
              root = TreeNode(preorder[0])
              left_value = preorder[1]
              right_value = postorder[-2]
              if left_value == right_value:
                  root.left = self.buildTree(preorder[2:], postorder[:-2])
                  root.right = None
                  return root
              print('preorder ', preorder)
              print('postorder ', postorder)
              print('left_value', left_value)
              print('right_value', right_value)
              post_index = postorder.index(left_value)
              pre_index = preorder.index(right_value)

              root.left = self.buildTree(preorder[1:pre_index], postorder[:post_index+1])
              root.right = self.buildTree(preorder[pre_index:], postorder[post_index+1:-1])
              return root
              
s=Solution()
preorder = [2, 1]
postorder = [1, 2]
s.constructFromPrePost(preorder=preorder,postorder=postorder)