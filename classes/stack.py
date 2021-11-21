import random


class Stack:
    def __init__(self):
        self.__stack = []
        print("Стек создан.")

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            print("Стек пуст.")

    def peak(self):
        try:
            print(self.__stack[len(self.__stack) - 1])
        except IndexError:
            print("Стек пуст.")

    def lenOfStack(self):
        return len(self.__stack)


stack = Stack()

for i in range(random.randint(1, 50)):
    stack.push(random.randint(0, 100))

stack.peak()

for i in range(stack.lenOfStack()):
    print(stack.pop(), end=' ')
print()

stack.pop()
stack.peak()

stack2 = Stack()

stack2.push(int(input()))

print(stack2.pop())
print(stack.pop())
