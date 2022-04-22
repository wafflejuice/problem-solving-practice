class MyHashMap:
    def __init__(self):
        self.mod = 10000
        self.my_keys = [[] for _ in range(self.mod)]
        self.my_values = [[] for _ in range(self.mod)]
        
    def hash(self, key):
        return key % self.mod
        
    def put(self, key: int, value: int) -> None:
        hash_idx = self.hash(key)
        keys_bucket = self.my_keys[hash_idx]
        values_bucket = self.my_values[hash_idx]
        
        if key in keys_bucket:
            key_idx = keys_bucket.index(key)
            values_bucket[key_idx] = value
        else:
            keys_bucket.append(key)
            values_bucket.append(value)

    def get(self, key: int) -> int:
        hash_idx = self.hash(key)
        keys_bucket = self.my_keys[hash_idx]
        values_bucket = self.my_values[hash_idx]
        
        if key in keys_bucket:
            key_idx = keys_bucket.index(key)
            return values_bucket[key_idx]
        return -1
        
    def remove(self, key: int) -> None:
        hash_idx = self.hash(key)
        keys_bucket = self.my_keys[hash_idx]
        values_bucket = self.my_values[hash_idx]
        
        if key in keys_bucket:
            idx = keys_bucket.index(key)
            keys_bucket.pop(idx)
            values_bucket.pop(idx)
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# operations = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# values = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# for op, input_ in zip(operations, values):
#     if op == "MyHashMap":
#         my_map = MyHashMap()
#         print('null', end=',')
#     elif op == "put":
#         my_map.put(input_[0], input_[1])
#         print("null", end=',')
#     elif op == "get":
#         val = my_map.get(input_[0])
#         print(val, end=',')
#     elif op == "remove":
#         my_map.remove(input_[0])
#         print("null", end=',')
# print()

operations2 = ["MyHashMap","remove","put","remove","remove","get","remove","put","get","remove","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","get","put","put","get","put","remove","remove","put","put","get","remove","put","put","put","get","put","put","remove","put","remove","remove","remove","put","remove","get","put","put","put","put","remove","put","get","put","put","get","put","remove","get","get","remove","put","put","put","put","put","put","get","get","remove","put","put","put","put","get","remove","put","put","put","put","put","put","put","put","put","put","remove","remove","get","remove","put","put","remove","get","put","put"]
values2 = [[],[27],[65,65],[19],[0],[18],[3],[42,0],[19],[42],[17,90],[31,76],[48,71],[5,50],[7,68],[73,74],[85,18],[74,95],[84,82],[59,29],[71,71],[42],[51,40],[33,76],[17],[89,95],[95],[30,31],[37,99],[51],[95,35],[65],[81],[61,46],[50,33],[59],[5],[75,89],[80,17],[35,94],[80],[19,68],[13,17],[70],[28,35],[99],[37],[13],[90,83],[41],[50],[29,98],[54,72],[6,8],[51,88],[13],[8,22],[85],[31,22],[60,9],[96],[6,35],[54],[15],[28],[51],[80,69],[58,92],[13,12],[91,56],[83,52],[8,48],[62],[54],[25],[36,4],[67,68],[83,36],[47,58],[82],[36],[30,85],[33,87],[42,18],[68,83],[50,53],[32,78],[48,90],[97,95],[13,8],[15,7],[5],[42],[20],[65],[57,9],[2,41],[6],[33],[16,44],[95,30]]
for op, input_ in zip(operations2, values2):
    if op == "MyHashMap":
        my_map = MyHashMap()
        print('null', end=',')
    elif op == "put":
        my_map.put(input_[0], input_[1])
        print("null", end=',')
    elif op == "get":
        val = my_map.get(input_[0])
        print(val, end=',')
    elif op == "remove":
        my_map.remove(input_[0])
        print("null", end=',')
print()