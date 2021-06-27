# recursion
# 1
def a():
    b ()
    print ('i am a function')


def b():
    c ()
    print ('i am b function')


def c():
    d ()
    print ('i am c function')


def d():
    print ('i am d function')


a ()


# 2
def num(n):
    if n >= 0:
        print (n)
        num (n - 1)
    else:
        print ('The recursion is done')


num (8)
print ('------------------------------------------')


def opp_num(n):
    if n >= 0:
        opp_num (n - 1)
        print (n)
    else:
        print ('The recursion is start')


opp_num (8)


# 3 Assertion error
def factorial(n):
    assert n >= 0 and int (n) == n, 'the no must be positive integer'
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)


print (factorial (8))


# 4 Fibonacci
def fibonacci(m):
    def method(n):
        if n in [0, 1]:
            return n
        else:
            return method (n - 2) + method (n - 1)

    if m > 0 and int (m) == m:
        fibonacci (m - 1)
        print (method (m - 1), end=',')


fibonacci (8)

# Arrays
# all in one
from array import *

my_array = array ('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in my_array:
    print (i)
print (len (my_array))
print (my_array[0])
my_array.append (11)
print (my_array)
my_array.insert (0, 0)
print (my_array)
array2 = array ('i', [11, 12, 13, 14])
my_array.extend (array2)
print (my_array)
my_list = [15, 16, 17, 18]
my_array.fromlist (my_list)
print (my_array)
my_array.append (18)
print (my_array)
my_array.remove (18)
print (my_array)
my_array.insert (2, 11)
print (my_array)
my_array.remove (11)
print (my_array)
my_array.pop ()
print (my_array)
print (my_array.index (11))
my_array.reverse ()
print (my_array)
print (my_array.buffer_info ())
print (my_array.count (11))
str = my_array.tostring ()  # convert it into string
print (str)
i = array ('i')
i.fromstring (str)
print (i)
a = my_array.tolist ()
print (a)
print (my_array[1:4])

# list
a = []
while (True):
    i = input ("Please enter value : ")
    if i == 'done': break
    b = float (i)
    a.append (b)

print (a)
print ('the avg is : ', sum (a) / len (a))


# Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, ):
        self.head = None

    def insert_new_head(self, new_node):
        new = Node (new_node)
        new.next = self.head
        self.head = new

    def insert_after(self, prev, new_node_1):
        if prev is None:
            print ('Previous Node is not present in list')
        else:
            new_1 = Node (new_node_1)
            new_1.next = prev.next
            prev.next = new_1

    def insert_at_end(self, new_node_2):
        new_2 = Node (new_node_2)
        temp = self.head
        if self.head == None:
            self.head = new_2
        while (temp.next != None):
            temp = temp.next
        temp.next = new_2

    def delete(self, key):
        temp = self.head
        if temp.value == key:
            self.head = temp.next
            temp = None
            return
        while (temp):
            prev = temp
            temp = temp.next
            if temp.value == key:
                prev.next = temp.next
                temp = None
                return

    def print_list(self):
        var = self.head
        while (var):
            print (var.value)
            var = var.next


if __name__ == '__main__':
    a = LinkedList ()
    a.head = Node (1)
    b = Node (2)
    c = Node (3)
    a.head.next = b
    b.next = c
    c.next = None
    a.insert_new_head (8)
    a.insert_new_head (9)
    a.insert_after (a.head, 16)
    a.insert_after (b.next, 85)
    a.insert_at_end (98)
    a.print_list ()
    a.delete (98)
    a.delete (16)
    a.print_list ()


# Stack


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len (self.data)

    def is_empty(self):
        return len (self.data) == 0

    def push(self, a):
        self.data.append (a)

    def top(self):
        if self.is_empty ():
            return ('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty ():
            raise Empty ('Stack is empty')
        self.data.pop ()

    def printing(self):
        return (self.data)


s = ArrayStack ()
print (s.top ())
s.push (8)
print (s)
s.push (7)
s.push (4)
s.push (9)
print (s.printing ())

# Queues
from queue import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def len(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def first(self):
        if self.isempty ():
            raise Empty ("Queue is empty")
        return self.data[self.front]

    def dequeue(self):
        if self.isempty ():
            raise Empty ("Queue is empty")
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len (self.data)
        self.size = self.size - 1
        return answer


s = ArrayQueue ()

# Queue own code
from queue import Empty


class ArrayQueue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len (self.data)

    def is_empty(self):
        return len (self.data) == 0

    def push(self, a):
        self.data.append (a)

    def first(self):
        if self.is_empty ():
            return ('Queue is empty')
        return self.data[0]

    def dequeue(self):
        if self.is_empty ():
            raise Empty ('Queue is empty')
        del self.data[0]

    def printing(self):
        return (self.data)


s=ArrayQueue()
s.push(8)
s.push(9)
s.push(7)
s.push(1)
print(s.printing())
s.dequeue()
print(s.printing())



#Binary Searched tree
class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class BinarySearchTree(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)


    def insertNode(self,data,node):
        if data<node.data:
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)


    def getMinValue(self):
        if self.root:
            return self.getMin (self.root)
    def getMin(self,node):
        if node.leftchild:
            return self.getMin(node.leftchild)
        else:
            return node.data


    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        else:
            return node.data


    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
    def traverseInOrder(self,node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)
        print(" %s " % node.data)
        if node.rightchild:
            self.traverseInOrder(node.rightchild)


a=BinarySearchTree()
a.insert(10)
a.insert(5)
a.insert(20)
a.insert(85)
print(a.getMaxValue())
a.traverse()




#AVL
class Node(object):
    def __init__(self):
        self.data=None
        self.height=0
        self.rightchild=None
        self.leftchild=None


class AVL(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self.inserNode(data,self.root)

    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data<node.data:
            node.leftchild=self.insertNode(data,node.leftchild)
        else:
            node.rightchild=self.insertNode(data,node.rightchild)

        node.height=max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1

        return self.settleViolation(data, node)


    def settleViolation(self,data,node):
        balance = self.calcBalance(node)

        # case 1 -> left left heavy situation
        if balance > 1 and data < node.leftchild.data:
            print("left left heavy situation ......")
            return self.RotateRight(node)

        #case 2  -> right right heavy situation
        if balance < -1 and data > node.rightchild.data:
            print('Right right heavy situation.....')
            return self.RotateLeft(node)

        if balance > 1 and data > node.leftchild.data:
            print('Left Right heavy situation.....')
            node.leftchild=self.RotateLeft(node.leftchild)
            return self.RotateRight(node)

        if balance < -1 and data < node.rightchild.data:
            print('Right Left heavy situation.....')
            node.rightchild=self.RotateRight(node.leftchild)
            return self.RotateLeft(node)







    def calcHeight(self,node):
        if not node:
            return -1
        return node.height

    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftchild)-self.calcHeight(node.rightchild)



    def RotateRight(self,node):
        print("Rotating to the right on node ", node.data)
        tempLeftChild=node.leftchild
        t=tempLeftChild.rightchild
        tempLeftChild.rightchild=None
        node.leftchild=t
        node.height=max( self.calcHeight(node.leftChild),self.calcHeight(node.rightchild))+1
        tempLeftChild.height=max(self.calcHeight(tempLeftChild.leftChild),self.calcHeight(tempLeftChild.rightchild))+1
        return tempLeftChild

    def RotateLeft(self,node):
        print("Rotating to the left on node ", node.data)
        tempRightChild=node.rightchild
        t=tempRightChild.leftchild
        tempRightChild.leftchild=None
        node.rightchild=t
        node.height=max( self.calcHeight(node.leftChild),self.calcHeight(node.rightchild))+1
        tempRightChild.height=max(self.calcHeight(tempRightChild.leftChild),self.calcHeight(tempRightChild.rightchild))+1
        return tempRightChild
