class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value


    def get(self, key: int) -> int:
        return self.hashmap[key] if key in self.hashmap else -1

    def remove(self, key: int) -> None:
        tempHash = {}
        for k, v in self.hashmap.items():
            if k == key and key in self.hashmap:
                continue
            else:
                tempHash[k] = v
        self.hashmap = tempHash


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)