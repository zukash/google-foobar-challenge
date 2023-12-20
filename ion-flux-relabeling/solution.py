class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def generate_perfect_binary_tree(h, start):
    subtree_size = 2 ** (h - 1) - 1
    root = Node(start + subtree_size * 2)
    if h > 1:
        root.left = generate_perfect_binary_tree(h - 1, start)
        root.right = generate_perfect_binary_tree(h - 1, start + subtree_size)
    return root


def solution(h, q):
    root = generate_perfect_binary_tree(h, 1)
    parent = {}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left.val] = node.val
            stack.append(node.left)
        if node.right:
            parent[node.right.val] = node.val
            stack.append(node.right)

    answer = []
    for val in q:
        assert 1 <= val < 2**h
        if val in parent:
            answer.append(parent[val])
        else:
            answer.append(-1)
    return answer
