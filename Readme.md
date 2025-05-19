# ☕ Coffee Shop Management System

A beginner-friendly Python project that simulates a coffee shop ordering system. This project demonstrates fundamental Object-Oriented Programming (OOP) concepts using three interconnected classes to model a real-world coffee shop scenario.


## 🎯 Project Overview

This Coffee Shop Management System is designed to help beginners understand:
- Object-Oriented Programming principles
- Class relationships and interactions
- Data validation and error handling
- Python best practices

The system models a simple coffee shop where customers can place orders for different types of coffee, and the shop can track which customers are the biggest spenders on specific coffee types.

## ✨ Features

- *Customer Management*: Create and manage customer profiles with validation
- *Coffee Inventory*: Define different coffee types with name validation
- *Order System*: Process orders linking customers to their coffee purchases
- *Analytics*: Find the biggest spender (aficionado) for any coffee type
- *Data Validation*: Built-in validation for names and inputs
- *Error Handling*: Descriptive error messages for invalid inputs

## 📁 Project Structure


coffee_shop/
├── customer.py          # Customer class definition
├── coffee.py            # Coffee class definition  
├── order.py             # Order class definition and main program
├── README.md            # This file

## 📚 Classes Documentation

### 🧑‍💼 Customer Class (customer.py)

*Purpose*: Represents a coffee shop customer who can place orders.

*Attributes*:
- name: Customer's name (1-15 characters, string only)
- orders: List of all orders placed by this customer
- all_customers: Class variable tracking all customers (shared across all instances)

*Methods*:
- __init__(name): Initialize a new customer
- create_order(coffee, price): Create a new order for this customer
- most_aficionado(coffee): Class method to find the biggest spender on a specific coffee type

*Validation Rules*:
- Name must be a string
- Name length must be between 1 and 15 characters

### ☕ Coffee Class (coffee.py)

*Purpose*: Represents a type of coffee available in the shop.

*Attributes*:
- name: Coffee type name (minimum 3 characters)

*Methods*:
- __init__(name): Initialize a new coffee type

*Validation Rules*:
- Name must be a string
- Name must be at least 3 characters long

### 🧾 Order Class (order.py)

*Purpose*: Represents a single order linking a customer to a coffee with a price.

*Attributes*:
- customer: The customer who placed the order
- coffee: The coffee type ordered
- price: The price of the order (automatically converted to float)

*Methods*:
- __init__(customer, coffee, price): Initialize a new order

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python and OOP concepts

### Installation Steps

1. *Clone the repository* (or download the files):
   bash
   git clone <repository-url>
   cd coffee_shop
   

2. *Set up a virtual environment* (recommended):
   bash
   # Create virtual environment
   python -m venv coffee_shop_env
   
   # Activate virtual environment
   # On Windows:
   coffee_shop_env\Scripts\activate
   # On macOS/Linux:
   source coffee_shop_env/bin/activate
   

3. *Install dependencies* (if any):
   bash
   pip install -r requirements.txt
   

4. *Verify installation*:
   bash
   python order.py

### Basic Usage

python
from customer import Customer
from coffee import Coffee

# Create customers
stacy = Customer("stacy")
bob = Customer("Bob")

# Create coffee types
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Create orders
order1 = alice.create_order(espresso, 3.50)
order2 = alice.create_order(latte, 4.50)
order3 = bob.create_order(espresso, 3.50)

# Find biggest espresso spender
biggest_fan = Customer.most_aficionado(espresso)
print(f"Biggest espresso fan: {biggest_fan.name}")


### Advanced Usage

python
# Multiple orders for same customer
customer = Customer("Coffee Lover")
americano = Coffee("Americano")

# Customer orders multiple americanos
for i in range(3):
    customer.create_order(americano, 3.00)

# Calculate total spent
total = sum(order.price for order in customer.orders)
print(f"{customer.name} spent ${total} total")


### Error Handling Examples

python
# These will raise ValueError exceptions:

# Invalid customer name
try:
    Customer("")  # Empty name
except ValueError as e:
    print(f"Error: {e}")

try:
    Customer("This name is way too long for validation")  # Name too long
except ValueError as e:
    print(f"Error: {e}")

# Invalid coffee name
try:
    Coffee("Ab")  # Too short
except ValueError as e:
    print(f"Error: {e}")


## 📊 Sample Output

When you run python order.py, you should see output similar to:


*** ***
The most aficionado for Espresso is: Wairimu
*** ***
Order created by: Wairimu
Coffee: Espresso, Price: $3.5
*** ***
Order created by: Natasha  
Coffee: Latte, Price: $4.5
*** ***
Order created by: Alex
Coffee: Cappuccino, Price: $4.25


## 🎓 Learning Objectives

By working with this project, you'll learn:

1. *Object-Oriented Programming*:
   - Class definition and instantiation
   - Instance vs class variables
   - Method definition and calling

2. *Data Validation*:
   - Input validation techniques
   - Custom error messages
   - Exception handling

3. *Relationships Between Classes*:
   - How objects interact with each other
   - Composition (Order contains Customer and Coffee)
   - Aggregation (Customer has many Orders)

4. *Python Concepts*:
   - List comprehensions
   - Class methods and decorators
   - Import statements and modules

## 🔧 Troubleshooting

### Common Issues

*Issue*: ModuleNotFoundError: No module named 'customer'
*Solution*: Make sure all files are in the same directory and you're running the script from that directory.

*Issue*: ValueError: Name must be a string between 1 and 15 characters
*Solution*: Check that customer names are strings with 1-15 characters.

*Issue*: AttributeError: 'Customer' object has no attribute 'orders'
*Solution*: Make sure you're creating Customer objects properly with Customer("name").

### Debugging Tips

1. *Print statements*: Add print statements to track program flow
2. *Check types*: Use type() and isinstance() to verify object types
3. *Validate inputs*: Always check that your inputs meet the class requirements

## 🤝 Contributing

We welcome contributions! Here are ways you can help:

1. *Report bugs*: Open an issue describing the problem
2. *Suggest features*: Propose new functionality
3. *Improve documentation*: Help make the README clearer
4. *Add tests*: Write unit tests for the classes
5. *Code improvements*: Submit pull requests with enhancements

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch: git checkout -b feature-name
3. Make your changes
4. Test your changes thoroughly
5. Submit a pull request with a clear description

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Thanks to all contributors who have helped improve this project
- Inspired by real-world coffee shop systems
- Created as an educational tool for learning Python and OOP

---

## 📞 Support

If you have questions or need help:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Usage Examples](#usage-examples)
3. Open an issue on GitHub
4. Contact the maintainers

*Happy coding! ☕✨*