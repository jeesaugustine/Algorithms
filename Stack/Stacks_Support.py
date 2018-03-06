#!/usr/bin/env python

"""
    This program simulates a two stack using a list of size n
    if the program was to do stack of total size of 'n-1' it was piece of cake but in this case in
    the edge condition there needs to be more careful design.
    There are two stacks accessed by push1 and push1 and pop1 and pop2
    They can store an maximum of 'n' elements in total at a given time and will give you no error but should work just
    fine
"""


__author__ = "Jees Augustine"
__copyright__ = "Copyright 2018,"
__credits__ = ["Jees Augustine"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Jees Augustine"
__email__ = "jees.augustine@mavs.uta.edu"
__status__ = "Learning"


class TwoStacks:
    def __init__(self, length):
        self.stack = [0] * length
        self.top1 = -1
        self.top2 = length
        self.empty1 = True
        self.empty2 = True
        self.length = length
        self.more_capacity = length
        self.stack1 = 0
        self.stack2 = 0

    def push1(self, val):
        if self.empty1:
            self.empty1 = False
        if self.more_capacity > 0:
            self.top1 += 1
            self.stack[self.top1] = val
            self.more_capacity -= 1
            self.stack1 += 1
        else:
            print('Stack is Full')

    def push2(self, val):
        if self.empty2:
            self.empty2 = False
        if self.more_capacity > 0:
            self.top2 += -1
            self.stack[self.top2] = val
            self.more_capacity -= 1
            self.stack2 += 1
        else:
            print('Stack is Full')

    def pop1(self):
        if self.stack1 > 0:
            val = self.stack[self.top1]
            self.top1 += -1
            self.more_capacity += 1
            self.stack1 -= 1
            return val
        if self.stack1 is 0:
            self.empty1 = False

        print('Nothing to pop')

    def pop2(self):
        if self.stack2 > 0:
            val = self.stack[self.top2]
            self.top2 += 1
            self.more_capacity += 1
            self.stack2 -= 1
            return val
        if self.stack2 is 0:
            self.empty1 = False
        print('Nothing to pop')


two_stacks = TwoStacks(5)

two_stacks.push2(1)
two_stacks.push2(2)
two_stacks.push2(3)
two_stacks.push2(4)
two_stacks.push2(5)

two_stacks.push2(6)
two_stacks.push1(7)

print(two_stacks.pop2())
print(two_stacks.pop1())

two_stacks.push1(8)
print(two_stacks.pop1())
print(two_stacks.pop1())
two_stacks.push2(9)
print(two_stacks.pop1())
print(two_stacks.pop2())
print(two_stacks.pop2())
print(two_stacks.pop2())
print(two_stacks.pop2())

print(two_stacks.pop2())

two_stacks.push1(1)
two_stacks.push1(2)
two_stacks.push1(3)
two_stacks.push1(4)
two_stacks.push1(5)

two_stacks.push2(6)

print()
