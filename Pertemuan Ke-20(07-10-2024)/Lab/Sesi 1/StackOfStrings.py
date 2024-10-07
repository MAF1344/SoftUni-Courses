class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)
        else:
            raise TypeError("Only strings can be added to the stack.")

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Stack is empty.")

    def top(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"