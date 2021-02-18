"""
https://leetcode.com/problems/implement-queue-using-stacks/description/

232. Implement Queue using Stacks

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Constraints:

    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.
"""

class MyQueue(object):

    def __init__(self):
        self.prim = []
        self.sec = []

    def push(self, x):
        self.sec.append(x)

    def pop(self):
        print ("sec=%s" % self.sec)
        print ("* prim=%s" % self.prim)
        if not self.prim:
            for i in range(len(self.sec)):
                self.prim.append(self.sec.pop())
            print ("prim=%s" % self.prim)
        x = self.prim.pop()
        print ('popped=%s' % x)
        return x
        

    def peek(self):
        if not self.prim:
            for i in range(len(self.sec)):
                self.prim.append(self.sec.pop())
        return self.prim[-1]
        

    def empty(self):
        x = bool(len(self.prim)) or bool(len(self.sec))
        return not x
	
        


