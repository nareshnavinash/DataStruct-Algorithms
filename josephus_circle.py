def josephus(n, k):
    if (n == 1):
        return 1
    else:
        available_arr = [i for i in range(1,n+1)]
        pointer = 0
        count = 0
        while count < n-1:
            for i in range(len(available_arr)):
                if available_arr[i] != None:
                    pointer = pointer + 1
                    if pointer % k == 0:
                        count = count + 1
                        available_arr[i] = None
        return list(filter(None, available_arr))[0]


n = 5
k = 2

print("The chosen place is ", josephus(n, k))


#####################################################################################################

def josephus(n, k):
    if (n == 1):
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

n = 14
k = 2

print("The chosen place is ", josephus(n, k))
