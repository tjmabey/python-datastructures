from node import Node

class Tree(object):
    '''A binary tree'''

    def __init__(self):
        self.root = None

    def add_node(self, key, value, current_node=None):
        '''add a node to the tree'''
        # if current_node is not passed in initially, then set it to the root
        if current_node is None:
            current_node = self.root

        # if the root is None, then create a Node and set it to the root and current_node
        if self.root is None:
            self.root = Node(key, value, Node('-', '-'))
        else:
            # traverse the tree
            if key >= current_node.key:
                if current_node.right is None:
                    current_node.right = Node(key, value, current_node)
                else:
                    self.add_node(key, value, current_node.right)
            elif key < current_node.key:
                if current_node.left is None:
                    current_node.left = Node(key, value, current_node)
                else:
                    self.add_node(key, value, current_node.left)


    def get(self, key):
        '''get a node by key'''
        return self._find(key, self.root)


    def remove(self, key):
        '''remove a node'''
        remove = self._find(key, self.root)
        # if the node exists
        if remove:
            # if the node has two children
            if remove.left and remove.right:
                # if there is a left branch off the right child
                if remove.right.left:
                    new_node = self._find_left_leaf(remove.right)
                    self._replace_node(remove, new_node)
                # if there is a right branch off the left child
                elif remove.left.right:
                    new_node = self._find_right_leaf(remove.left)
                    self._replace_node(remove, new_node)
                # if there are no values in 'middle' then just move up the node.right
                else:
                    self._replace_node(remove, remove.right)
            # if the node only has a left child
            elif remove.left:
                remove.parent.left = remove.left
                remove.left.parent = remove.parent
                if remove == self.root:
                    self.root = remove.left
            # if the node only has a right child
            elif remove.right:
                remove.parent.right = remove.right
                remove.right.parent = remove.parent
                if remove == self.root:
                    self.root = remove.right
            # if leaf node
            else:
                if self._is_left_node(remove):
                    remove.parent.left = None
                else:
                    remove.parent.right = None
        else:
            # if the node to remove is not found then just return
            return


    def _find(self, key, node):
        '''find a node in the tree'''
        if node is None:
            return None

        if node.key == key:
            return node
        elif key < node.key:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)


    def _replace_node(self, old_node, new_node):
        '''replace a node'''
        # if the old node was the root
        if old_node == self.root:
            self.root = new_node

        # detach the new node from the tree
        if self._is_left_node(new_node):
            new_node.parent.left = None
        else:
            new_node.parent.right = None
        new_node.parent = old_node.parent

        # if the old node was a left child
        if self._is_left_node(old_node):
            # set old node parent left to new node
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        new_node.left = old_node.left
        new_node.left.parent = new_node
        new_node.right = old_node.right
        new_node.right.parent = new_node


    def _find_left_leaf(self, node):
        '''check if the node has a left leaf'''
        if node.left:
            return self._find_left_leaf(node.left)
        else:
            return node


    def _find_right_leaf(self, node):
        '''check if the node has a right leaf'''
        if node.right:
            return self._find_right_leaf(node.right)
        else:
            return node


    def _is_left_node(self, node):
        '''returns true if the node is a left child of its parent'''
        return node.parent.key > node.key


    def walk_dfs_inorder(self, node=None):
        '''returns an inorder dfs traversal of the tree as a list'''
        li = []
        if node is None:
            node = self.root

        if node.left:
            li += self.walk_dfs_inorder(node.left)

        li.append(node.value)

        if node.right:
            li += self.walk_dfs_inorder(node.right)

        return li


    def walk_dfs_preorder(self, node=None):
        '''returns a preorder dfs traversal of the tree as a list'''
        li = []
        if node is None:
            node = self.root

        li.append(node.value)

        if node.left:
            li += self.walk_dfs_preorder(node.left)

        if node.right:
            li += self.walk_dfs_preorder(node.right)

        return li


    def walk_dfs_postorder(self, node=None):
        '''returns a postorder dfs traversal of the tree as a list'''
        li = []
        if node is None:
            node = self.root

        if node.left:
            li += self.walk_dfs_inorder(node.left)

        if node.right:
            li += self.walk_dfs_inorder(node.right)

        li.append(node.value)

        return li


    def walk_bfs(self):
        '''returns a bfs traversal (left to right) of the tree as a list'''
        q = []
        q.append(self.root)
        li = []

        while len(q) > 0:
            node = q.pop(0)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            li.append(node.value)

        return li


    def debug_print(self):
        '''
        print a "graphical" representation of the tree. note that spacing is
        not accurately represented.
        '''
        current_level = [self.root]
        tree = []

        while current_level:
            next_level = []
            for l in current_level:
                tree.append('{}({}){}'.format(l.key, l.parent.key, '\t'))
                if l.left:
                    next_level.append(l.left)
                if l.right:
                    next_level.append(l.right)
            tree.append('\n')
            current_level = next_level

        print(''.join(tree))
