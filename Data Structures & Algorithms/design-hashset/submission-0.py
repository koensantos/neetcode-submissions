class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        curr_set = list(self.hashset)
        curr_set.append(key)
        self.hashset = set(curr_set)

    def remove(self, key: int) -> None:
        new_set = []
        for val in self.hashset:
            if val != key:
                new_set.append(val)
        self.hashset = set(new_set)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)