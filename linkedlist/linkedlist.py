#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        # this is not very efficient, btw
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print('{} >>> {}'.format(self.size, ', '.join(values)))

    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if index < 0 or index >= self.size:
            raise IndexError('{} is not within the bounds of the current list.'.format(index))


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self._check_bounds(index)
        h = self.head

        for i in range(0, index):
            h = h.next

        return h


    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is None:
            self.head = Node(item)
        else:
            h = self.head

            while h.next is not None:
                h = h.next

            h.next = Node(item)

        self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        previous = self._get_node(index - 1)
        after = previous.next
        previous.next = Node(item)
        previous.next.next = after
        self.size += 1


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self._get_node(index)
        n.value = item


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        # check bounds first
        self._check_bounds(index)
        n = self.head
        for i in range(0, index):
           n = n.next
        return n.value


    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if index is 0:
            self.head = self.head.next
        else:
            # previous is the node previous to the node getting deleted
            previous = self._get_node(index - 1)

            # previous.next is set to the node after the node getting deleted
            previous.next = self._get_node(index).next
        self.size -= 1


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''

        node1 = self.get(index1)
        node2 = self.get(index2)

        self.set(index1, node2)
        self.set(index2, node1)



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
