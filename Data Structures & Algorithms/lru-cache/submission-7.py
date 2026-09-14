class LRUCache:

    def __init__(self, capacity: int):
        self.order_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.order_dict:
            return -1

        self.order_dict.move_to_end(key)

        return self.order_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.order_dict:
            self.order_dict.move_to_end(key)
            self.order_dict[key] = value
            return
        if self.capacity <= len(self.order_dict):
            self.order_dict.popitem(last=False)

        self.order_dict[key] = value