# Tyler Mabey
# 15 Sep 2017
#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0
        self.chunk_size = chunk_size


    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if 0 <= index and index < self.size:
            pass
        else:
            raise IndexError


    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if len(self.data) == self.size:
            new_array = alloc(self.size + self.chunk_size)
            self.data = memcpy(new_array, self.data, len(self.data))


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        empty_chunks = int((len(self.data) - self.size) / 5)
        if empty_chunks > 0:
            new_array = alloc(len(self.data) - (self.chunk_size * empty_chunks))
            self.data = memcpy(new_array, self.data, len(new_array))


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()
        self.data[self.size] = item
        self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        index = int(index)
        self._check_bounds(index)
        self.add(item)
        for node in range(self.size - 1, index, -1):
            self.swap(node, node - 1)


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        index = int(index)
        self._check_bounds(index)
        self.data[index] = item


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        index = int(index)
        self._check_bounds(index)
        if self.data[index] is not None:
            return self.data[index]


    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        index = int(index)
        self._check_bounds(index)
        self.data[index] = None

        for node in range(0, self.size - 1):
            if self.data[node] is None:
                self.swap(node, node + 1)

        self.size -= 1
        self._check_decrease()


    def swap(self, index1, index2):
        index1 = int(index1)
        index2 = int(index2)
        '''Swaps the values at the given indices.'''
        self._check_bounds(index1)
        self._check_bounds(index2)
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp


###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    new_array = []
    for i in range(size):
        new_array.append(None)

    return new_array


def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    for node in range(0, size):
        dest[node] = source[node]

    return dest
