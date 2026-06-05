class stack():
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==0
    def push(self,elements):
        self.items.append(elements)
    def pop(self):
        if self. isempty():
            return "stack is empty"
        return self.items.pop()
    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.items[-1]
    def display(self):
        return self.items
    def size (self):
        return len(self.items)

s=stack()
print("push operations")
s.push(10)
s.push(20)
s.push(30)
print("stack size is:",s.size())
print("content of the stack are:",s.display())
print("peek items is:",s.peek())
s.pop()
s.pop()
print("contents of the stack are:",s.display())
print("stack size is:",s.size())
print("peek item is;",s.peek())
