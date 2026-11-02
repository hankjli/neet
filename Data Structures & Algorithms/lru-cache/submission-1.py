class Node:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key to val
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.key_to_node = {}

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # kv pair exists
        target = self.key_to_node[key]
        target.next.prev = target.prev
        target.prev.next = target.next

        temp = self.dummy_head.next
        target.next = temp
        target.prev = self.dummy_head
        self.dummy_head.next = target
        temp.prev = target

        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key already in cache, just update value
            self.cache[key] = value
            target = self.key_to_node[key]
            target.next.prev = target.prev
            target.prev.next = target.next

            temp = self.dummy_head.next
            target.next = temp
            target.prev = self.dummy_head
            self.dummy_head.next = target
            temp.prev = target
        else:
            # must add new kv pair
            if len(self.cache) >= self.capacity:
                # cache is full, must evict lru kv pair
                # lru node stored in tail.prev

                node_to_remove = self.dummy_tail.prev

                self.dummy_tail.prev = node_to_remove.prev
                self.dummy_tail.prev.next = self.dummy_tail

                del self.cache[node_to_remove.key]
                del self.key_to_node[node_to_remove.key]

            # can just add the value regularly
            self.cache[key] = value

            new_node = Node(value, key)
            self.key_to_node[key] = new_node

            # was the most recent access, add to front of dll
            temp = self.dummy_head.next

            new_node.next = temp
            temp.prev = new_node # temp != None bc of dummy
            self.dummy_head.next = new_node
            new_node.prev = self.dummy_head
    
