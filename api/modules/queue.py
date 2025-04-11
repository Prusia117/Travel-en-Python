#** Esto es una cola de prioridad, que se utiliza para almacenar los nodos y sus distancias. **#
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def extract_min(self):
        if not self.is_empty():
            min_index = 0
            for i in range(1, len(self.items)):
                if self.items[i][1] < self.items[min_index][1]:
                    min_index = i
            min_item = self.items[min_index]
            self.items.pop(min_index)
            return min_item[0]

    def decrease_key(self, node, new_priority):
        for i in range(len(self.items)):
            if self.items[i][0] == node:
                self.items[i] = (node, new_priority)
                break

    def is_empty(self):
        return len(self.items) == 0