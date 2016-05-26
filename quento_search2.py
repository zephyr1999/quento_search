# searches where both operations and numbers are nodes
class Board:
    # The board is arranges as follows:
    #
    #   a0  b0  a1
    #   b1  a2  b2
    #   a3  b3  a4
    #
    # where the a's are numbers from the board and the bs are operations.
    # b0 : +, b1 : -, b2 : -, b3 : +

    def __init__(self,a0,a1,a2,a3,a4):
        self.nums = (a0,a1,a2,a3,a4)
        self.named={'a0':a0,'a1':a1,'a2':a2,'a3':a3,'a4':a4}
        # name the root node 'root' because it is a special case for the algorithm
        self.root = Node('root')
        self.tree = build_tree(self.root)

    def depth_value_search(self,depth,value):
        '''depth is the count of numbers to use for the value, value is the actual thing we're searching for'''
        self.print_seq(search(self,depth*2-1,value,self.tree))

    def print_seq(self,sequence):
        '''prettily prints the sequence returned from the search'''
        if sequence is None:
            print("Error: none found")
            return
        for c in sequence[1:]:
            # the root has index 0, so skip it
            if c.startswith('a'):
                # c is a value node in the tree
                print(self.named[c],end=" ")
            elif c.endswith(('1','2')):
                # c is a compute node, particularly a subtract node
                print('-',end=" ")
            else:
                # c is an add compute node
                print('+',end=" ")

def search(b,depth,value,tree):
    '''searches through the tree to the depth specified for the value'''
    if depth==0 and tree.get_value(b)==value:
        # we have reached the target node, so return the sequence
        return tree.seq + [tree.name]
    elif depth==0:
        # we have reached the specified depth, but found nothing
        return None
    else:
        for child in tree.children:
            # recursively call on children, decrementing the depth
            res = search(b,depth-1,value,child)
            if res is not None:
                # once a target is found, return and exit the loop
                return res
        return None

def build_tree(start_node,depth=1):
    '''constructs a tree from a root node'''
    if depth>=12:
        # we have reached the maximum depth for quento searching
        return start_node
    else:
        for child in start_node.get_children():
            if child not in start_node.seq:
                # if a node is a child and has not been seen already,
                # create a new Node object and give it children
                n = Node(name=child)
                n.seq=(start_node.seq + [start_node.name])
                start_node.children.append(n)
        for child in start_node.children:
            # recursively build the tree
            build_tree(child,depth+1)
        return start_node


class Node:
    '''represents a node of the search tree. can have a type, as specified 
    by its name:
    -root is the root of the tree
    -'a' is a value node, holing one of the numbers
    -'b' is a compute node reptresenting add of subtract'''
    def __init__(self,name,seq=[]):
        self.name = name
        self.seq = seq
        self.children = []

    def get_value(self,b):
        # uses b Board to calculate value based on sequence
        # each sequence should go [root,a,b,a,b...]
        val = 0
        # add self's name to the sequence because if not, it would never check the leaf nodes
        l = self.seq + [self.name]
        for c in l[1::2]:
            # the cryptic line above iterates over every other index, starting with one,
            # like 1,3,5... 
            # this is done because the 0 index is the root, so skip that,
            # and then the even indicies are operations
            #iterate over every a value, using the previous b value to select operation
            if l[l.index(c)-1].endswith('1') or l[l.index(c)-1].endswith('2'):
                # in english: if the node in the sequence before me ends in
                # a 1 or 2, then it is a subtract node
                val = val - b.named[c]
            else:
                # otherwise, it is an add node.
                # note that just using 'else' here solves the problem of the root node
                # being named 'root' and needing all additions
                val = val + b.named[c]
        return val

    def get_children(self):
        '''returns the adjacent nodes as defined by the quento board.'''
        if self.name == 'a0':
            return ['b0','b1']
        elif self.name == 'a1':
            return ['b0','b2']
        elif self.name == 'a2':
            return ['b0','b1','b2','b3']
        elif self.name == 'a3':
            return ['b3','b1']
        elif self.name == 'a4':
            return ['b3','b2']
        elif self.name == 'b0':
            return ['a0','a1','a2']
        elif self.name == 'b1':
            return ['a0','a3','a2']
        elif self.name == 'b2':
            return ['a4','a1','a2']
        elif self.name == 'b3':
            return ['a4','a3','a2']
        else:
            # root node, return all a's
            return ['a0','a1','a2','a3','a4']


