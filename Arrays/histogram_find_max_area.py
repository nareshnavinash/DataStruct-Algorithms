# O(n)
def find_max_area(arr):
    length = len(arr)
    i = 0
    max_val = 0
    area = 0
    index_stack = []

    while i < length:
        if index_stack == [] or arr[index_stack[-1]] <= arr[i]:
            index_stack.append(i)
            i += 1
        else:
            top_index = index_stack.pop()
            if not index_stack:
                area = arr[top_index] * i
            else:
                area = arr[top_index] * (i - index_stack[-1] - 1)
        max_val = max(max_val, area)

    print(max_val)


a = [6, 2, 5, 4, 5, 1, 6]
find_max_area(a)
