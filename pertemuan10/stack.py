from collections import deque

stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')
stack.appendleft('D')
stack.popleft()
print(stack)