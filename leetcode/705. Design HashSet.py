class MyHashSet:
    def __init__(self):
        self.mod = 10000
        self.hash_list = [set() for _ in range(self.mod)]
        
    def add(self, key: int) -> None:
        self.hash_list[key % self.mod].add(key)
        
    def remove(self, key: int) -> None:
        self.hash_list[key % self.mod].discard(key)
        
    def contains(self, key: int) -> bool:
        return key in self.hash_list[key % self.mod]
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

operations = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
values = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
for op, key in zip(operations, values):
    if op == "MyHashSet":
        my_set = MyHashSet()
        print('None', end=' ')
    elif op == "add":
        my_set.add(key[0])
        print("None", end=' ')
    elif op == "remove":
        my_set.remove(key[0])
        print("None", end=' ')
    elif op == "contains":
        is_containing = my_set.contains(key[0])
        print(is_containing, end=' ')
print()