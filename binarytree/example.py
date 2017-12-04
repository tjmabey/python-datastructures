'''
Tyler Mabey

this is an example that you can run to see the binary tree working in action

'''

from tree import Tree

t = Tree()

li = {
    'c': 'C',
    'h': 'H',
    'a': 'A',
    'e': 'E',
    'f': 'F',
    'd': 'D',
    'b': 'B',
    'j': 'J',
    'g': 'G',
    'i': 'I',
    'k': 'K'
}
for key, value in li.items():
    t.add_node(key, value)

print('Initial tree:')
t.debug_print()

print('\nLookups:')
print(t.get('f').value)
print(t.get('b').value)
print(t.get('i').value)

print('\nBFS:')
print(t.walk_bfs())

print('\nDFS preorder:')
print(t.walk_dfs_preorder())

print('\nDFS inorder:')
print(t.walk_dfs_inorder())

print('\nDFS postorder:')
print(t.walk_dfs_postorder())

print('\nRemove b:')
t.remove('b')
t.debug_print()

print('\nRemove f:')
t.remove('f')
t.debug_print()

print('\nRemove h:')
t.remove('h')
t.debug_print()
