def check_balance(text):
    open_braces = tuple("(,{,[")
    close_braces = tuple("),},]")
    map = dict(zip(open_braces, close_braces))
    queue = []

    for i in text:
        if i in open_braces:
            queue.append(map[i])
        elif i in close_braces:
            if not queue or i != queue.pop():
                return False
    return False if queue else True


print(check_balance("([{()}])"))
