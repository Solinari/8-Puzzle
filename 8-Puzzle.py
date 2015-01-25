# Justin Tyme Dejesus
# AI 380/480
# Assignment 1

# The book's website: http://aima-python.googlecode.com/svn/trunk/search.py
# has a wonderful template for general abstracts of node & problem
# I will be adapting and implementing these for the assignment's purpose
# because the general methods are so general and abstract already.
# the real work is in problem and the searches anyhow


# Node class

class Node:

    def __init__(self, state, parent = None, action = None,
                 path_cost = 0, depth = 0):
        '''instantiate the node but also the root if first node
        also handles how the graph to the goal is formed'''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

        #set depth
        if parent:
            self.depth = parent.depth + 1

        # add more...
    def child_node(self, problem, action):
        '''pass a problem object to store in the child '''

        #this returns state
        is_next = problem.result(self.state, action)

        #return cost
        is_cost = problem.path_cost()

        # think about parent...
        # I think since you don't pass it, it's not none
        # and self is the pointer because it is a class object
        # and has implicit __iter__ and __next__
        # I still think you need to pass it..
        return Node(self, is_next, action, is_cost, depth, parent = self)

    def path(self):
        '''return the path from root to current node'''
        this_node = self
        the_path = []

        while node:
            the_path.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        ''' return the solution along a path'''
        sol = [node.action for node in self.path()[1:]]

        return sol

    def __eq__(self, other):
        '''returns checking to see if states are the same
        and if both are Nodes'''
        is_node = isinstance(other, Node)

        return is_node and self.state == other.state
        
    
    def __repr__(self):
        '''return the state in the node'''
        return "Node {}".format(self.state)




# class BFS - using this as my Parent class for the searches

class BFS:

    def __init__(self):
        '''intitalizes queue'''
        self.q = []

    def isEmpty(self):
        '''returns if queue is empty'''
        return len(self.q) == 0

    def enqueue (self, item):
        '''appends an item to queue'''
        return self.q.append(item)

    def dequeue(self):
        '''checks if empty, if not deappends an item'''
        # Remember we are comparing the return of a class method
        # against a boolean condition
        
        if self.isEmpty == True:
            return 'Queue is empty'

        else:
            return self.q.pop(0)

    def __eq__(self, other):
        '''checks if self.q == other.q'''
        return self.q == other.q

    def __len__(self):
        '''overloaded operator to take the length on self.q'''
        return len(self.q)

    def __repr__(self):
        '''define how to represent this object canonically'''
        # shell will call repr on variables
        return 'Queue: {}'.format(self.q)

    def __str__(self):
        '''represent the self.q object in string form'''
        # print() will call on this overloaded method
        return 'Queue is: {}'.format(self.q)

#some tests

# base Class tests

# BFS tests
kew = BFS()

kew.enqueue(100)
print(kew)

print(kew.dequeue())
    
print(kew)

print(len(kew))

# Node Tests
node = Node([0, 1, 2])

print(node)
        

# extend to superclass dfs




