# Jees Augustine 
# Code for combined stack of size 'n' and has two separte stacks within


class Stack:
    def __init__(self, length):
        self.stack = [0 ] *length
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

