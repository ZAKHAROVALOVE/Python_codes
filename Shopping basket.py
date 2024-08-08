#Class for product description. Fields: price value, description, product dimensions.
#Class "Buyer". Fields: surname, first name, patronymic, mobile phone, etc.
#Order class. An order may contain several products, and the quantity of each product may be different.
# The order must be "linked" to the user who placed it.
#Implement a method for calculating the total cost of an order.
# Define the str() method to correctly output information about this order.
#12.2
class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user: User):
        self.products = {}
        self.user = user

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = cnt

    def get_total(self) -> float:
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self) -> str:
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"


if __name__ == "__main__":
    lemon = Item('lemon', 5, "yellow", "small")
    apple = Item('apple', 2, "red", "middle")
    print(lemon)  # lemon, price: 5

    buyer = User("Ivan", "Ivanov", "02628162")
    print(buyer)

    cart = Purchase(buyer)
    cart.add_item(lemon, 4)
    cart.add_item(apple, 20)
    print(cart)

    assert isinstance(cart.user, User) is True, 'An instance of the User class'
    assert cart.get_total() == 60, "A total of 60"
    assert cart.get_total() == 60, 'There should be 60 left!'
    cart.add_item(apple, 10)
    print(cart)

    assert cart.get_total() == 40