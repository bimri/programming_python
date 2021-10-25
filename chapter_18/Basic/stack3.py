"Optimization: Tuple Tree Stacks"
'optimize with tuple pair trees'
'''
One way to speed up such code is to change the underlying data structure completely.
For example, we can store the stacked objects in a binary tree of tuples: each item may
be recorded as a pair, (object, tree), where object is the stacked item and tree is
either another tuple pair giving the rest of the stack or None to designate an empty stack.
A stack of items
'''
class Stack:
    def __init__(self, start=[]):              # init from any sequence
        self.stack = None                      # even other (fast)stacks
        for i in range(-len(start), 0):
            self.push(start[-i - 1])           # push in reverse order

    def push(self, node):                      # grow tree 'up/left'
        self.stack = node, self.stack          # new root tuple: (node, tree)

    def pop(self):
        node, self.stack = self.stack          # remove root tuple
        return node                            # TypeError if empty

    def empty(self):
        return not self.stack                  # is it 'None'?

    def __len__(self):                         # on: len, not
        len, tree = 0, self.stack
        while tree:
            len, tree = len+1, tree[1]         # visit right subtrees
        return len

    def __getitem__(self, index):              # on: x[i], in, for
        len, tree = 0, self.stack
        while len < index and tree:            # visit/count nodes
            len, tree = len+1, tree[1]
        if tree:
            return tree[0]                     # IndexError if out-of-bounds
        else: 
            raise IndexError()                 # so 'in' and 'for' stop

    def __repr__(self): 
        return '[FastStack:' + repr(self.stack) + ']'

"""
Because we add or remove only a top tuple to push and pop items, this structure
avoids copying the entire stack. For large stacks, the benefit might be significant.
"""
