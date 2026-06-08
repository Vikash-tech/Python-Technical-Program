from collections import deque


# Q1. MinStack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Q2. Evaluate Postfix Expression
def eval_postfix(tokens):
    stack = []

    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))

    return stack[0]


# Q3. Queue Using Two Stacks
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def front(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]


# Q4. Daily Temperatures
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx

        stack.append(i)

    return result


# Q5. Infix to Postfix
def infix_to_postfix(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    stack = []
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in precedence:
            while (stack and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


# Q7. Validate Stack Sequences
def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0

    for x in pushed:
        stack.append(x)

        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return not stack


# Q8. MaxStack
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]

    def popMax(self):
        max_val = self.peekMax()
        buffer = []

        while self.top() != max_val:
            buffer.append(self.pop())

        self.pop()

        while buffer:
            self.push(buffer.pop())

        return max_val


if __name__ == "__main__":

    print("===== Q1 MinStack =====")
    ms = MinStack()

    ms.push(-2)
    ms.push(0)
    ms.push(-3)

    print("Min:", ms.getMin())
    ms.pop()
    print("Top:", ms.top())
    print("Min:", ms.getMin())

    print("\n===== Q2 Postfix Evaluation =====")
    expr = ["2", "1", "+", "3", "*"]
    print(eval_postfix(expr))

    print("\n===== Q3 Queue Using Two Stacks =====")
    q = MyQueue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.front())

    print("\n===== Q4 Daily Temperatures =====")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temps))

    print("\n===== Q5 Infix To Postfix =====")
    exp = "3 + 4 * 2"
    print(infix_to_postfix(exp))

    print("\n===== Q6 LIFO vs FIFO =====")

    print("""
            LIFO (Stack):
            Last In First Out

            Examples:
            - Browser Back Button
            - Undo Operation
            - Function Call Stack

            FIFO (Queue):
            First In First Out

            Examples:
            - Ticket Counter
            - Printer Queue
            - Customer Service Line

            Choose Stack:
            - Undo/Redo
            - DFS
            - Expression Evaluation

            Choose Queue:
            - Scheduling
            - BFS
            - Task Processing
       """)

    print("===== Q7 Validate Stack Sequences =====")
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

    print(validate_stack_sequences(pushed, popped))

    print("\n===== Q8 MaxStack =====")
    mx = MaxStack()

    mx.push(5)
    mx.push(1)
    mx.push(5)

    print("Top:", mx.top())
    print("Max:", mx.peekMax())
    print("PopMax:", mx.popMax())
    print("Top:", mx.top())
    print("Max:", mx.peekMax())