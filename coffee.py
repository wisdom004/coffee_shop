class Coffee:
    def _init_(self,name):

        if not isinstance(name, str) or not (3 <= len(name)):
            raise ValueError("Coffee name must be a string greater than 3 characters")
        
        self.name = name
        self.orders = []

    def order(self):
        return self.order
    
    def add_item(self, item):
        self.orders.append(item)
    
    def get_coffee_items(self):
        ordered = set()
        coffee_list = []
        for item in self.orders:
            if item not in ordered:
                coffee_list.append(item)
                ordered.add(item)
        return coffee_list