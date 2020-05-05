def replace_with_nearest_greater_element(array):
    length = len(array)
    result = []
    max_element = -1
    for i in range(length - 1, 0, -1):
        if not result:
            max_element = array[i]
            result.insert(0, array[i])
        else:
            max_element = max(max_element, array[i])
            result.insert(0, max_element)
    print(result)


array = [6, 23, 46, 7, 8, 89, 75, 10]
replace_with_nearest_greater_element(array)
