class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        lines = []
        title = f"{self.category:*^30}"
        lines.append(title)
        for item in self.ledger:
            description = item['description'][:23]
            amount = item['amount']
            amount_str = f"{amount:.2f}"
            lines.append(f"{description:<23}{amount_str:>7}")
        total = self.get_balance()
        lines.append(f"Total: {total:.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_percentages = []
    category_names = []

    # Calculate total withdrawals for percentage calculation
    total_withdrawals = 0
    for category in categories:
        withdrawals = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_percentages.append(withdrawals)
        total_withdrawals += withdrawals
        category_names.append(category.category)

    # Calculate percentages and create the chart
    percentages = [(spent / total_withdrawals) * 100 for spent in spent_percentages]
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add bottom line and category names
    chart += "    ----------\n     "
    max_length = max(len(name) for name in category_names)
    for i in range(max_length):
        for name in category_names:
            if i < len(name):
                chart += f"{name[i]}  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n     "

    # Remove trailing spaces
    if chart[-1] == "\n":
        chart = chart[:-1]

    return chart


# Example Usage and Testing
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)  # Print the ledger for Food category

categories = [food, clothing]
print(create_spend_chart(categories))  # Print the spending chart

