# Stock Span O(n)
def find_span(arr):
    length = len(arr)
    span = [0 for i in range(length)]
    span[0] = 1
    index = [0]

    for i in range(1, length):
        span[i] = 1
        while len(index) > 0 and arr[index[-1]] <= arr[i]:
            index.pop()
        if len(index) > 0:
            span[i] = i - index[-1]
        else:
            span[i] = i + 1
        index.append(i)
    print(span)


# O(n^2)
def span(arr):
    length = len(arr)
    span = [0 for i in range(length)]
    span[0] = 1

    for i in range(1, length):
        span[i] = 1
        j = i - 1
        while j >= 0 and arr[i] >= arr[j]:
            j = j - 1
            span[i] += 1

    print(span)


a = [10, 4, 5, 90, 120, 80]
find_span(a)
span(a)
