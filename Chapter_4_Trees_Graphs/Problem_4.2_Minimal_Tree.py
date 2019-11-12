class TreeNode:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.data) + " R:" + str(self.right) + ')'

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def call_to_minimal_tree_array(arr):
    return minimal_tree_array(arr, 0, len(arr) - 1)

def minimal_tree_array(arr, start, end):
    if end < start:
        return ''

    mid = (start + end) // 2

    root = TreeNode(arr[mid])

    root.left = minimal_tree_array(arr, start, mid - 1)

    root.right = minimal_tree_array(arr, mid + 1, end)

    return root


# testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
testArray = [3, 5, 9, 11, 14, 19]
print(call_to_minimal_tree_array(testArray))

