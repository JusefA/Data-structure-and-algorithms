class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def check_balance(text):
    stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    open_brackets = set(bracket_pairs.values())
    close_brackets = set(bracket_pairs.keys())
    error_position = -1
    pairs_count = 0

    for i, char in enumerate(text, start=1):
        if char in open_brackets:
            stack.push((char, i))
        elif char in close_brackets:
            if stack.is_empty():
                return f"Match error at position {i-1}"
            top = stack.pop()
            if bracket_pairs[char] != top[0]:
                return f"Match error at position {i-1}"
            pairs_count += 1
        else:
            continue

    if not stack.is_empty():
        error_position = stack.pop()[1]

    if error_position != -1:
        return f"Match error at position {error_position-1}"
    else:
        return f"Ok - {pairs_count}"

