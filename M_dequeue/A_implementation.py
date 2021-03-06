class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    """
    from timeit import timeit

    obj = Deque()
    print(timeit(lambda: obj, number=10000)) # 0.0005975749954814091
    """
