class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(data=1, left=Node(data=3, left=Node(data=7, left=Node(0)), right=Node(6)), 
                    right=Node(data=2, left=Node(5), right=Node(4)))