class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False
        self.mushroom = False
        self.onion = False
        self.peppers = False
        self.sauce = None

    def __str__(self):
        return f"Size: {self.size}, Cheese: {self.cheese}, Pepperoni: {self.pepperoni}, Bacon: {self.bacon}, Mushroom: {self.mushroom}, Onion: {self.onion}, Peppers: {self.peppers}, Sauce: {self.sauce}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def add_mushroom(self):
        self.pizza.mushroom = True
        return self

    def add_onion(self):
        self.pizza.onion = True
        return self

    def add_peppers(self):
        self.pizza.peppers = True
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def build(self):
        return self.pizza


def client():

    builder = PizzaBuilder()
    pizza = (
        builder.set_size("Large")
        .add_cheese()
        .add_pepperoni()
        .add_bacon()
        .add_mushroom()
        .add_onion()
        .add_peppers()
        .set_sauce("Tomato")
        .build()
    )
    print(pizza)


if __name__ == "__main__":
    client()
