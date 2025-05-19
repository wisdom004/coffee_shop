class Customer:
    all_customers = []
    def _init_(self, name):

        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)
        
    
    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)  
        self.orders.append(order)  
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spend = 0

        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders if order.coffee == coffee)

            if total > max_spend:
                max_spent = total
                top_customer = customer

        return top_customer if max_spent > 0 else None