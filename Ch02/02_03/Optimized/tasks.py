"""Task queue - deque example"""
from collections import deque
from queue import Queue


class TaskQueue:
    """Task queue using list"""

    def __init__(self):
        self._tasks = []

    def push(self, task):
        self._tasks.insert(0, task)

    def pop(self):
        return self._tasks.pop()

    def __len__(self):
        return len(self._tasks)


class TaskQueue2:
    """Task queue using list"""

    def __init__(self):
        self._tasks = []

    def push(self, task):
        self._tasks.append(task)

    def pop(self):
        return self._tasks.pop(0)

    def __len__(self):
        return len(self._tasks)


class DTaskQueue:
    """Task queue using deque"""

    def __init__(self):
        self._tasks = deque()

    def push(self, task):
        self._tasks.append(task)

    def pop(self):
        return self._tasks.popleft()

    def __len__(self):
        return len(self._tasks)


class QTaskQueue:
    """Task queue using Queue"""

    def __init__(self) -> None:
        self._tasks = Queue()

    def push(self, task):
        self._tasks.put(task)

    def pop(self):
        return self._tasks.get()

    def __len__(self):
        return self._tasks.qsize()


def test_queue(count=100, cls=TaskQueue):
    tq = cls()

    for i in range(count):
        tq.push(i)
        assert len(tq) == i + 1

    for i in range(count):
        assert tq.pop() == i
        assert len(tq) == count - i - 1


if __name__ == "__main__":
    test_queue(cls=TaskQueue)
    test_queue(cls=TaskQueue2)
    test_queue(cls=DTaskQueue)
    test_queue(cls=QTaskQueue)
