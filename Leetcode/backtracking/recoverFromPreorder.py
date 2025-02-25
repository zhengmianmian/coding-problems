import re
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(dic, i=1):
        if i not in dic or dic[i]==0:  # Handle out of bounds or null nodes
            return None

        root = TreeNode(dic[i])
        root.left = build_tree(dic, 2 * i)  # Left child
        root.right = build_tree(dic, 2 * i + 1)  # Right child
        return root
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        dic={}
        numDashes = self.getDashesAndNum(traversal)
        print('numDashes: ', numDashes)
        positions = []
        # traversal = "1-401--349---90--88"
        # [[1, 0], [401, 1], [349, 2], [90, 3], [88, 2]]
        layers=0
        for i in range(len(numDashes)):
            print('positions: ', positions)
            if numDashes[i][1] > layers:
                layers = numDashes[i][1]
            if numDashes[i][1] == 0:
                dic[1] = numDashes[i][0]
                positions.append(1)
            if i>0:
              # child
              if numDashes[i][1] == numDashes[i-1][1]+1:
                  last_index = positions[len(positions)-1]
                  dic[last_index * 2] = numDashes[i][0]
                  positions.append(last_index * 2)
              # neighbor
              elif numDashes[i][1] == numDashes[i-1][1]:
                  last_index = positions[len(positions)-1]
                  dic[last_index + 1] = numDashes[i][0]
                  positions.append(last_index + 1)
              # go back to find the parent
              elif numDashes[i][1] < numDashes[i-1][1]:
                  root=0
                  for j in range(i-2, -1, -1):
                      if numDashes[j][1]+1 == numDashes[i][1]:
                          root = j
                          break
                  dic[positions[root] * 2 + 1] = numDashes[i][0]
                  positions.append(positions[root] * 2 + 1)
       
        root = build_tree(dic)
        return root

    
    def getDashesAndNum(self, traversal):
        matches = re.findall(r'(-*)(\d+)', traversal)
        print('matches: ', matches)
        result = [[int(num), len(dashes)] for dashes, num in matches]
        return result
    
s=Solution()
r = s.recoverFromPreorder("1-401--349---90--88")
print(r)