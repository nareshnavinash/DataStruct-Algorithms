def precedence(sign):
    if sign == "+" or sign == "-":
        return 1
    elif sign == "*" or sign == "/":
        return 2
    elif sign == "^":
        return 3
    else:
        return 0


def compute(val1, val2, op):
    if op == "+":
        return int(val1) + int(val2)
    elif op == "-":
        return int(val1) - int(val2)
    elif op == "*":
        return int(val1) * int(val2)
    elif op == "/":
        return int(val1) / int(val2)
    elif op == "^":
        return int(val1) ^ int(val2)
    else:
        return "Not a proper operator"


def evaluate(string):
    operator = ["+", "-", "*", "/", "^"]
    stack_operator = []
    values = []
    length = len(string)
    i = 0
    while i < length:
        print("operator stack --- ")
        print(stack_operator)
        print("values stack --- ")
        print(values)
        if string[i] == " ":
            i += 1
        elif string[i].isnumeric():
            temp = string[i]
            try:
                while string[i + 1].isnumeric():
                    temp = temp + string[i + 1]
                    i += 1
            except:
                print("out of range")
            values.append(temp)
            i += 1
        elif string[i] in operator:
            while stack_operator and stack_operator[- 1] in operator and precedence(stack_operator[- 1]) > precedence(string[i]):
                a = values.pop()
                b = values.pop()
                c = stack_operator.pop()
                temp = compute(b, a, c)
                values.append(temp)
            stack_operator.append(string[i])
            i += 1
        elif string[i] == "(":
            stack_operator.append(string[i])
            i += 1
        elif string[i] == ")":
            while len(stack_operator) != 0 and stack_operator[-1] != "(":
                a = values.pop()
                b = values.pop()
                c = stack_operator.pop()
                temp = compute(b, a, c)
                values.append(temp)
            if len(stack_operator) != 0 and stack_operator[-1] == "(":
                stack_operator.pop()
            else:
                print("Invalid expression")
            i += 1
        else:
            print("Invalid operators present")

    while stack_operator:
        print("operator stack --- ")
        print(stack_operator)
        print("values stack --- ")
        a = values.pop()
        b = values.pop()
        c = stack_operator.pop()
        temp = compute(b, a, c)
        values.append(temp)

    return values[0]


print(evaluate("100 * ( 2 + 12 )"))
print(evaluate("10 + 2 * 6"))
print(evaluate("100 * 2 + 12"))
print(evaluate("100 * ( 2 + 12 ) / 14"))
print(evaluate("( 1 + 10 ) * ( 4 - 2 )"))

