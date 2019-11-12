class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class List_of_Depts:

    def call_to_minimal_tree_array(self, arr):
        return self.minimal_tree_array(arr, 0, len(arr) - 1)

    def minimal_tree_array(self, arr, start, end):
        if end < start:
            return ''

        mid = (start + end) // 2

        root = TreeNode(arr[mid])

        root.left = self.minimal_tree_array(arr, start, mid - 1)

        root.right = self.minimal_tree_array(arr, mid + 1, end)

        return root

    def create_lists_per_level(self, node, depth, levels=[]):

        if not node:
            return

        if depth == 0:
            levels.append(Node(node.value))
        else:
            if depth >= len(levels):
                levels.append(Node(node.value))
            else:

                linked_element_at_index = levels[depth]
                while linked_element_at_index:
                    previous = linked_element_at_index
                    linked_element_at_index = linked_element_at_index.next

                previous.next = Node(node.value)

        self.create_lists_per_level(node.left, depth + 1, levels)
        self.create_lists_per_level(node.right, depth + 1, levels)

        return levels

    def create_lists_per_levelV2(self, bst):

        current = bst

        queue = []

        result = []

        level = 0

        if current:
            result.append([current])
        else:
            return []

        while True:
            if not result[level]:
                break

            result.append([])

            for n in result[level]:

                if n.left:
                    result[level + 1].append(n.left)
                if n.right:
                    result[level + 1].append(n.right)

            level += 1

        return result

initialize = List_of_Depts()

bst = initialize.call_to_minimal_tree_array(list(range(0,8)))

print(list(range(0,8)))

linked_list = initialize.create_lists_per_level(bst, 0)

print(linked_list)

result = initialize.create_lists_per_levelV2(bst)

print(result)















