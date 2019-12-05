# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        a = self.lca_t(A,B,C)
        if a:
            return a.val
        return -1
    def lca_t(self, A, B, C):
        if A and self.has_child(A, B) and self.has_child(A, C):
            n = self.lca_t(A.left, B, C)
            if not n:
                n = self.lca_t(A.right, B, C)
            if not n:
                return A
            return n
        return None
        
    def has_child(self, A, val):
        if not A:
            return False
        return A.val == val or self.has_child(A.right, val) or self.has_child(A.left, val)
