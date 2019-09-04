class Pizza:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.size = ""
        self.crust_type = ""
        self.topping = []

    def add_topping(self, topping):
        self.topping.append(topping)

    def print_order(self):
        connector = " and "
        print(f'I would like a {self.size}-inch, {self.crust_type} pizza with {connector.join(self.topping)}')



meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust_type = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Sausage")
meat_lovers.print_order()

veggie = Pizza()
veggie.size = 12
veggie.crust_type = "Hand tossed"
veggie.add_topping("Artichoke")
veggie.add_topping("Olives")
veggie.print_order()