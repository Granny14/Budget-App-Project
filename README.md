# Budget-App-Project

# Description
- **The Budget App is a Python project that helps you manage and visualize your expenses across different categories. You can create categories, deposit funds, withdraw funds, transfer money between categories, and generate a chart to visualize your spending.**

# Features
- **Category Management: Create and manage different categories like Food, Clothing, Entertainment, etc.**
- **Deposit and Withdrawal: Easily deposit and withdraw money within a category, with an optional description.**
- **Transfer Funds: Transfer money between categories.**
- **Spend Chart: Generate a bar chart showing the percentage of spending in each category.**

# Classes and Methods
## Category Class
- **This class represents a budget category and contains the following methods:**

- **__init__(self, category): Initializes a category with an empty ledger.**
- **deposit(self, amount, description=""): Adds a deposit entry to the ledger.**
- **withdraw(self, amount, description=""): Adds a withdrawal entry to the ledger if there are sufficient funds.**
- **get_balance(self): Returns the current balance of the category.**
- **transfer(self, amount, category): Transfers an amount from one category to another if there are sufficient funds.**
- **check_funds(self, amount): Checks if there are enough funds in the category for a withdrawal or transfer.**
- **__str__(self): Returns a string representation of the category's ledger.**
- **create_spend_chart(categories) Function**
- **This function takes a list of Category objects and generates a bar chart representing the percentage of spending in each category.**

# Example Usage and Testing
- **food = Category("Food")**
- **food.deposit(1000, "initial deposit")**
- **food.withdraw(10.15, "groceries")**
- **food.withdraw(15.89, "restaurant and more food for dessert")**

- **clothing = Category("Clothing")**
- **food.transfer(50, clothing)**

**print(food)  # Print the ledger for Food category**

**categories = [food, clothing]**
**print(create_spend_chart(categories))  # Print the spending chart**

# Output:

*************Food*************
initial deposit        1000.00
groceries              -10.15
restaurant and more foo-15.89
Transfer to Clothing   -50.00
Total: 923.96

# Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|    o     
 40|    o     
 30|    o     
 20|    o     
 10|    o     
  0| o  o     
    ----------
     F  C  
     o  l  
     o  o  
     d  t  
           h  
           i  
           n  
           g  

# Installation
- **To use this project, clone the repository to your local machine:**

- **git clone https://github.com/your-username/budget-app.git**
- **Then, navigate to the project directory and run your Python script.**

# Running Tests
- **You can create additional test cases to verify the functionality of the Category class and the create_spend_chart function.**

# Contributing
- **Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit an issue or a pull request.**

# License
- **This project is licensed under the MIT License - see the LICENSE file for details.**
