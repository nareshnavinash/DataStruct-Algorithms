class Stack:

    def __init__(self):
        self.array = []
        self.top = -1

    def push(self, data):
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

    def clear(self):
        while self.top != -1:
            self.array.pop()


class FormulaConvert(Stack):

    def __init__(self):
        super().__init__()
        self.output = []
        self.stack = Stack()
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        self.braces = {"(": ")", "{": "}", "[": "]"}

    def isNotGreaterOrEqual(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.stack.peek()]
            return True if a <= b else False
        except:
            return False

    def reverse_string_without_braces(self, string):
        string = string[::-1]
        final_string = ""
        for i in string:
            if i in self.braces.keys():
                final_string = final_string + self.braces[i]
            elif i in self.braces.values():
                final_string = final_string + list(self.braces.keys())[list(self.braces.values()).index(i)]
            else:
                final_string = final_string + i
        return final_string

    def infixToPostfix(self, string):
        print("\nInfix to postfix \n\nString --- " + string + "\n")
        for i in string:
            if i.isalpha():
                self.output.append(i)
            elif i in self.braces.keys():
                self.stack.push(self.braces[i])
            elif i in self.braces.values():
                while (not self.stack.isempty()) and (self.stack.peek() != i):
                    temp = self.stack.pop()
                    self.output.append(temp)
                if not self.stack.isempty() and self.stack.peek() != i:
                    return False
                else:
                    self.stack.pop()
            else:
                while not self.stack.isempty() and self.isNotGreaterOrEqual(i):
                    self.output.append(self.stack.pop())
                self.stack.push(i)

        while not self.stack.isempty():
            self.output.append(self.stack.pop())

        result = "".join(self.output)
        print(result)
        self.stack.clear()
        self.output.clear()
        return result

    def infixToPrefix(self, string):
        final_string = self.reverse_string_without_braces(string)

        print("\nInfix to Prefix \n\nString --- " + final_string + "\n")
        result = self.infixToPostfix(final_string)
        print(result[::-1])
        return result[::-1]

    def postfixToInfix(self, string):
        print("\nPostfix to infix --- " + string)
        for i in string:
            if i.isalpha():
                self.output.insert(0, i)
            else:
                a = self.output[0]
                self.output.pop(0)
                b = self.output[0]
                self.output.pop(0)
                self.output.insert(0, "(" + b + i + a + ")")
        result = self.output[0]
        self.output.clear()
        print(result)
        return result

    def prefixToInfix(self, string):
        final_string = string[::-1]
        print("\nPrefix to infix --- " + final_string)
        result = self.reverse_string_without_braces(self.postfixToInfix(final_string))
        self.output.clear()
        print(result)
        return result

    def prefixToPostfix(self, string):
        print("\nPrefix to postfix --- " + string + "\n")
        string = string[::-1]
        for i in string:
            if not i.isalpha():
                a = self.output.pop()
                b = self.output.pop()
                temp = a + b + i
                self.output.append(temp)
            else:
                self.output.append(i)
        result = "".join(self.output)
        print(result)
        self.output.clear()
        return result

    def postfixToPrefix(self, string):
        print("\nPostfix to Prefix --- " + string + "\n")
        for i in string:
            if not i.isalpha():
                a = self.output.pop()
                b = self.output.pop()
                temp = i + b + a
                self.output.append(temp)
            else:
                self.output.append(i)
        result = "".join(self.output)
        print(result)
        self.output.clear()
        return result


exp = "a+b*(c^d-e)^(f+g*h)-i"
conv = FormulaConvert()
postfix = conv.infixToPostfix(exp)
prefix = conv.infixToPrefix(exp)
conv.prefixToInfix(prefix)
conv.prefixToPostfix(prefix)
conv.postfixToPrefix(postfix)
