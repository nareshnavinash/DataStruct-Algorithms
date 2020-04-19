def is_valid_cell(Arr, r, c, traversed, row, column):
    if r >= 0 and r < row and c >=0 and c < column and Arr[r][c] == 1 and not traversed[r][c]:
        return True
    else:
        return False



def run_through_nodes(Arr, r, c, traversed, count, row, column):
    possible_rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    possible_cols = [-1, 0, 1, 1, -1, -1, 0, 1]
    traversed[r][c] = True

    for k in range(8):
            if is_valid_cell(Arr, r + possible_rows[k], c + possible_cols[k], traversed, row, column):
                count[0] +=1
                run_through_nodes(Arr, r + possible_rows[k], c + possible_cols[k], traversed,count, row, column)



def find_largest_path(Arr):
    if len(Arr) == 0 or len(Arr[0]) == 0:
        return 0

    row = len(Arr)
    column = len(Arr[0])

    traversed = [[0] * column for i in range(row)]
    count = [0]
    result = -1
    for i in range(row):
        for j in range(column):
            if Arr[i][j] == 1 and traversed[i][j] != True:
                count[0] = 1
                run_through_nodes(Arr,i,j,traversed,count,row, column)
                result = max(result, count[0])

    return result


Arr = [[1,1,0,1,0],
       [0,0,0,1,0],
       [0,1,0,1,0],
       [0,1,0,1,0],
       [0,1,0,1,0]]

print(find_largest_path(Arr))



####################################################################################################################
def is_valid(arr, i, j, traversed, row, col):
    if row > i >= 0 and col > j >= 0 and traversed[i][j] != True and arr[i][j] == 1:
        return True


def find_area(arr, i, j, row, column, count, traversed):
    possible_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    possible_col = [-1, 0, 1, -1, 1, -1, 0, 1]
    traversed[i][j] = True

    for k in range(len(possible_row)):
        if is_valid(arr, i + possible_row[k], j + possible_col[k], traversed, row, column):
            count[0] += 1
            find_area(arr, i + possible_row[k], j + possible_col[k], row, column, count, traversed)

def find_largest_area(arr):
    row = len(arr)
    if row == 0: return 0
    column = len(arr[0])
    if column == 0: return 0

    traversed = [[0] * column for i in range(row)]
    result = -1
    count = [0]
    for i in range(row):
        for j in range(column):
            if arr[i][j] == 1 and traversed[i][j] != True:
                count[0] = 1
                find_area(arr, i, j, row, column, count, traversed)
                result = max(result, count[0])
    return(result)


a = [[1, 0, 0, 0, 1],
     [1, 1, 0, 0, 1],
     [0, 1, 0, 0, 1],
     [0, 1, 1, 0, 1],
     [0, 1, 1, 0, 1]]

print(find_largest_area(a))
