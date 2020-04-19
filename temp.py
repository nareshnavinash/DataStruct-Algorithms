class Stack:

    def __init__(self):
        self.array =[]
        self.top = -1

    def push(self, data):
        print("pushing -- " + data)
        self.array.append(data)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        else:
            a = self.array[self.top]
            del self.array[self.top]  # self.array.pop()
            self.top -= 1
            return a

    def peek(self):
        return self.array[-1]

    def length(self):
        return len(self.array)

    def isempty(self):
        return self.top == -1

class FormulaConvert(Stack):

    def __init__(self):
        super().__init__()
        self.output = []
        self.stack = Stack()
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        self.braces = {"(": ")", "{": "}", "[": "]"}

    def isNotGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.stack.peek()]
            return True if a <= b else False
        except:
            return False

    def infixToPostfix(self, string):
        print("String ---" + string)
        for i in string:
            if i.isalpha():
                print("alphabets --- " + i)
                self.output.append(i)
            elif i in self.braces.keys():
                print("openbraces --- " + i)
                self.stack.push(self.braces[i])
            elif i in self.braces.values():
                print("closebraces --- " + i)
                while (not self.stack.isempty()) and (self.stack.peek() != i):
                    temp = self.stack.pop()
                    print("Appending to output --- " + temp)
                    self.output.append(temp)
                if not self.stack.isempty() and self.stack.peek() != i:
                    return False
                else:
                    self.stack.pop()
            else:
                print("Operators --- " + i)
                while not self.stack.isempty() and self.isNotGreater(i):
                    self.output.append(self.stack.pop())
                self.stack.push(i)

        while not self.stack.isempty():
            self.output.append(self.stack.pop())

        print("".join(self.output))


exp = "a+b*(c^d-e)^(f+g*h)-i"
conv = FormulaConvert()
conv.infixToPostfix(exp)
