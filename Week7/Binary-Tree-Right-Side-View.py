# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        deque = collections.deque()
        if root:
            deque.append(root)
        result = []
        while deque:
            size, val = len(deque), 0
            for i in range(size):
                node = deque.popleft()
                val = node.val
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            result.append(val)
        return result
