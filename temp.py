def compute(val1, val2, op):
    if op == "+":
        return int(val1) + int(val2)
    elif op == "-":
        return int(val1) - int(val2)
    elif op =="*":
        return int(val1) * int(val2)
    elif op == "/":
        return int(val1) / int(val2)
    elif op == "^":
        return int(val1) ^ int(val2)
    else:
        return "Not a proper operator"


def evaluate(string):
    braces = {"(": ")"}
    operator = ["+", "-", "*", "/", "^"]
    stack_braces = []
    stack_operator = []
    values = []
    length = len(string)
    i = 0
    while i < length:
        print("braces stack --- ")
        print(stack_braces)
        print("operator stack --- ")
        print(stack_operator)
        print("values stack --- ")
        print(values)
        if string[i] == " ":
            i += 1
        elif string[i].isnumeric():
            temp = string[i]
            while string[i + 1].isnumeric():
                temp = temp + string[i + 1]
                i += 1
            values.append(temp)
            i += 1
        elif string[i] in operator:
            stack_operator.append(string[i])
            i += 1
        elif string[i] in braces.keys():
            stack_braces.append(string[i])
            i += 1
        elif string[i] in braces.values():
            if len(stack_braces) != 0 and stack_braces[-1] in braces.keys():
                a = values.pop()
                b = values.pop()
                c = stack_operator.pop()
                temp = compute(b, a, c)
                values.append(temp)
                stack_braces.pop()
                i += 1
            else:
                print("Invalid expression")
        else:
            print("Invalid operators present")

    while stack_operator:
        print("braces stack --- ")
        print(stack_braces)
        print("operator stack --- ")
        print(stack_operator)
        print("values stack --- ")
        a = values.pop()
        b = values.pop()
        c = stack_operator.pop()
        temp = compute(b, a, c)
        values.append(temp)

    return values[0]





a = "( 1 + 10 ) * ( 4 - 2 )"
print(evaluate(a))