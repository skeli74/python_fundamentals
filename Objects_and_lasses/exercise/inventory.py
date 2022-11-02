class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []
        self.counter_capacity = self.__capacity

    def add_item(self, item: str):
        self.item = item

        if self.__capacity > len(self.items):
            self.items.append(self.item)
            self.counter_capacity -= 1

        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.counter_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
