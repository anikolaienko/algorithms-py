from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        node = self

        while node:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(value)
                    break

        return self


def in_order(root: Node):
    result = []
    node = root
    stack = deque()
    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        result.append(node.value)

        node = node.right
    
    return result


def pre_order(root: Node):
    result = []
    node = root
    stack = deque()
    while node or len(stack):
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        node = node.left if node.left else (stack.pop() if len(stack) else None)
    
    return result


def post_order(root: Node):
    result = []
    node = root
    stack = deque()
    right_child_stack = deque()
    while node or len(stack):
        if node:
            if node.right:
                right_child_stack.append(node.right)
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if len(right_child_stack) and right_child_stack[-1] == node.right:
                node = right_child_stack.pop()
            else:
                result.append(stack.pop().value)
                node = None
    return result