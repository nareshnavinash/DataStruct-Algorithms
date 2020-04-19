def reverse(arr, count):
    temp = []
    for i in range(int(len(arr)/count) + 1):
        try:
            rev_temp = []
            for i in range(count):
                rev_temp.append(arr[0])
                arr.remove(arr[0])
            rev_temp.reverse()
            temp = temp + rev_temp
        except:
            rev_temp.reverse()
            temp = temp + rev_temp
            return temp
    return temp


a = [1,2,3,4,5,6,7,8,9,10]
b = 2
print(reverse(a,b))


#############################################################################################

def reverse(arr, count):
    temp = []
    start = 0
    while start < len(arr):
        if len(arr[start:]) < count:
            temp = temp + list(reversed(arr[start:]))
            break
        temp = temp + list(reversed(arr[start:start+count]))
        start = start + count
    return temp


a = [1,2,3,4,5,6,7,8,9,10]
b = 2
print(reverse(a,b))
