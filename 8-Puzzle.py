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

        #return cost - this is kind of like abstract method tucking
        is_cost = problem.path_cost(self.path_cost, self.state, action, is_next)

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

# Problem class

class Problem(Node):

    def __init__(self, initial, goal = None):
        '''stating state and remember to pass goal to problem'''
        self.initial = initial
        self.goal = goal

    # IMPLEMENT ACTIONS AND RESULT!! AFTER THIS G2G on BFS STATE TESTING!
    # this part I am making specifically for the 8-puzzle. ie it won't be abstract

    def actions(self, state):
        '''return availible actions
        this is the real meat of defining the child nodes
        this will pass a list of the child Nodes to result'''

        # So here is where 0 is in the state
        # do I just want to make 9 cases? (all 9 positions
        z = state.index(0)

        if state[0] == z:
            pass

        if state[1] == z:
            pass

        if state[2] == z:
            pass

        if state[3] == z:
            pass

        if state[4] == z:
            pass

        if state[5] == z:
            pass

        if state[6] == z:
            pass

        if state[7] == z:
            pass

        if state[8] == z:
            pass

    def result(self, state, action):
        '''returns an action from self.actions(state)'''
        pass

    def goal_test(self, state):
        '''returns boolean of if state == goal'''

        return state == self.goal

    def path_cost(self, cost, state_one, action, state_two):
        '''defines current path cost'''
        
        return cost + 1


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
# setting the lists like this lets me
# visualize 
node1 = Node([1, 2, 3,
              8, 0, 4,
              7, 6, 5])

print(node1)

node2 = Node([1, 2, 3,
              8, 0, 4,
              7, 6, 5])

node3 = Node([1, 2, 3,
              8, 6, 4,
              7, 0, 5])


print(node1.__eq__(node2))
print(node2.__eq__(node3))
print(node1.__eq__(node3))

# extend to superclass dfs




