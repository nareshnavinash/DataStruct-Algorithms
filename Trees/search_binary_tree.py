class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def findElement(root, element):
    if root is None:
        return False
    if root.data == element:
        return True
    if findElement(root.left, element):
        return True
    if findElement(root.right, element):
        return True
    return False


# Driver Code
if __name__ == '__main__':
    root = newNode(-2)
    root.left = newNode(-7)
    root.right = newNode(-5)
    root.left.right = newNode(-6)
    root.left.right.left = newNode(-1)
    root.left.right.right = newNode(-11)
    root.right.right = newNode(-9)
    root.right.right.left = newNode(-4)

    print("serach element is", findElement(root, -90))
    q = []
    q.append(root)
    print(q.pop())
