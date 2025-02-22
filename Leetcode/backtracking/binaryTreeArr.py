# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.arr=[0]
        self.root = root
        root.val = 0
        self.recover(root)

    def recover(self, root):
        if root.left:
            root.left.val = root.val * 2 + 1
            self.arr.append(root.left.val)
            self.recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.arr.append(root.right.val)
            self.recover(root.right)
       
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.arr:
            return True
        return False
        
  

# Your FindElements object will be instantiated and called as such:
obj = FindElements(root)
param_1 = obj.find(target)