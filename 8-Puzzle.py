# Justin Tyme Dejesus
# AI 380/480
# Assignment 1

# class Queue - using this as my Parent class for the searches

class Queue:

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
kew = Queue()

kew.enqueue(100)
print(kew)

print(kew.dequeue())


# Node class

class Node():

    def __init__(self, state, parent = None, PathCost = 0):
        '''instantiate the node'''

        # add more...
        

# extend to superclass BFS

class BFS(Queue):
    '''inherits from Queue to be a Breadth-First Search'''

    
print(kew)

print(len(kew))
