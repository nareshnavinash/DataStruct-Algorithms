def remove_consecutive_duplicates(string):
    result = ""
    i = 0
    length = len(string)
    while i < length:
        if (i + 1) < length and string[i] == string[i+1]:
            i += 2
        else:
            print(string[i])
            result = result + string[i]
            i += 1
    print(result)

def remove_consecutive_duplicates_iteratively(string):
    result = []
    i = 0
    length = len(string)
    while i < length:
        if not result or result[-1] != string[i]:
            result.append(string[i])
            i += 1
        else:
            while result and result[-1] == string[i]:
                result.pop()
            i += 1
    print("".join(result))


string = "abbaca"
remove_consecutive_duplicates(string)
remove_consecutive_duplicates_iteratively(string)
