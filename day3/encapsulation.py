class Item:

    def __init__(self, item_name: str = "unknown", item_price: int =1):
        self.__item_name = None   #private
        self.__item_price = None   #private
        self.set_item_name(item_name)
        self.set_item_price(item_price)

    def get_item_name(self) -> str:
        return self.__item_name

    def get_item_price(self):
         return self. __item_price

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_price(self, item_price: int):
        if item_price < 0:
            raise RuntimeError(f"Item price cannot be negative or zero: {item_price}")
        self.__item_price = item_price


item1 = Item()

print(item1.get_item_name())
item1.set_item_name("Laptop")
item1.set_item_price(1234)

print(item1.get_item_name())
#print(item1.get_item_price())

item2 = Item("Phone", 800)
print(item2.get_item_name())
print(item2.get_item_price())

