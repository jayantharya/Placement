stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print("Stack:",stack)
#print("top element:",stack[-1])
popped=stack.pop()
print("popped:",popped)
print("stack after pop:",stack)
popped=stack.pop()
print("popped:",popped)
print("stack after pop:",stack)
stack.append(5)
print("stack:",stack)
print("top element:",stack[-1])
print("is empty:",len(stack)==0)

#stack using class
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
s=Stack()
s.push('a');s.push('b');s.push('c')
print(s.peek())
print(s.pop())
s.push('d');s.push('e')
print(s.pop())
print(s.peek())
    