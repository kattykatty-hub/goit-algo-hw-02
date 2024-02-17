from collections import deque

s = input()
QUEUE = deque(s)

palindrom = True

while len(QUEUE) > 1:
    first = QUEUE.popleft()
    last = QUEUE.pop()
    if first != last:
        palindrom = False
        break

print(
    f"{s=}",
    f"{palindrom=}"
)
