class Stack:
    def __init__(self,limit):
        self.s=[]
        self.limit=limit
    def empty(self):
        if self.s:
            return False
        else:
            return True
    def full(self):
        if len(self.s)==self.limit:
            return True
        else:
            return False
    def push(self,elem):
        if self.full():
            return "The stack has been FULL!"            
        else:
            self.s.append(elem)
            return self.s            
    def pop(self):
        if self.empty():
            return "The stack has been EMPTY!"
        else:
            self.s.pop()
            return self.s
    def find(self,x):
        if x in self.s:
            for i in range(len(self.s)):
                if self.s[i]==x:
                    return i
        else:
            return "The stack has no elem"+' '+str(x)
    def peek(self):
        if self.empty():
            return "The stack is empty"
        else:
            return self.s[::-1][0]
