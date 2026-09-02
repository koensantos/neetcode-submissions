class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.used = [] #stores keys
    def get(self, key: int) -> int:
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            removed = self.used.pop(0)
            del self.cache[removed]
            self.used.append(key)
            self.cache[key] = value
        else:
            if key in self.cache:
                self.used.remove(key)
                self.used.append(key)
                self.cache[key] = value
            else:
                self.used.append(key)
                self.cache[key] = value
