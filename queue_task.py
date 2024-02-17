import random
from collections import deque
from uuid import uuid4

# Створити чергу заявок
QUEUE = deque()


def generate_request():
    request = uuid4()
    QUEUE.append(request)
    print(f"{request}; додана в чергу")


def process_request():
    if QUEUE:
        request = QUEUE.popleft()
        print(f"{request}; заявка оброблена")
    else:
        print("Черга пуста")


if __name__ == '__main__':
    while True:
        if not input():  # для зручності демонстрації просто нажиматимемо enter

            # щоб просто не було створили обробили, добавили трошки рандому
            if random.choice([True, False]):
                generate_request()
            else:
                process_request()
