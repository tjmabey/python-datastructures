from linkedlist import LinkedList

class Processor(object):

    def run(self, f):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):
            # get the line parts
            line = line.rstrip()
            print('{}:{}'.format(line_i, line))
            parts = line.split(',')
            # call this command's function
            try:
                func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
                func(*parts[1:])
            except Exception as e:
                print('Error: {}'.format(e))

    def cmd_debug(self, *args):
        self.linked.debug_print()

    def cmd_create(self, *args):
        self.linked = LinkedList()

    def cmd_add(self, *args):
        self.linked.add(args[0])

    def cmd_insert(self, *args):
        self.linked.insert(int(args[0]), args[1])

    def cmd_set(self, *args):
        self.linked.set(int(args[0]), args[1])

    def cmd_get(self, *args):
        print(self.linked.get(int(args[0])))

    def cmd_delete(self, *args):
        self.linked.delete(int(args[0]))

    def cmd_swap(self, *args):
        self.linked.swap(int(args[0]), int(args[1]))

#######################
###   Main loop

with open('data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)
