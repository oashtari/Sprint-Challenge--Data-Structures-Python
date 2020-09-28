
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):

        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.next
        
        else:
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head 
            self.current.value = item

    def get(self):
        buffer_data = []

        item = self.storage.head

        while item is not None:
            buffer_data.append(item.value)
            item = item.next

        return buffer_data


