class Node(object):
    '''A node'''

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return "{}({})".format(self.key, self.parent.key)
