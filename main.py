import math


class Category:
    """
    A class to represent a budget category.
    Handles deposits, withdrawals, transfers, and balance tracking.
    """

    def __init__(self, name):
        """
        Initialize a new budget category.
        
        Args:
            name (str): The name of the budget category.
        """
        self.name = name
        self.ledger = []      # List to store all transactions
        self.balance = 0      # Current available balance
        self.spent = 0        # Total amount spent (for chart calculation)
    
    def deposit(self, amount, description=''):
        """
        Add funds to the category.
        
        Args:
            amount (float): The amount to deposit.
            description (str): Optional description for the transaction.
        """
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self.balance += amount

    def withdraw(self, amount, description=''):
        """
        Withdraw funds from the category if sufficient funds exist.
        
        Args:
            amount (float): The amount to withdraw.
            description (str): Optional description for the transaction.
        
        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if self.check_funds(amount) == True:
            self.ledger.append({
                'amount': -1 * amount,
                'description': description
            })
            self.balance += -1 * amount
            self.spent += amount
            return True
        return False
    
    def get_balance(self):
        """
        Get the current balance of the category.
        
        Returns:
            float: The current balance.
        """
        return self.balance
    
    def transfer(self, amount, category):
        """
        Transfer funds from this category to another category.
        
        Args:
            amount (float): The amount to transfer.
            category (Category): The destination category object.
        
        Returns:
            bool: True if transfer was successful, False otherwise.
        """
        if self.withdraw(amount, f'Transfer to {category.name}') == True:
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        """
        Check if there are sufficient funds for a transaction.
        
        Args:
            amount (float): The amount to check against balance.
        
        Returns:
            bool: True if funds are sufficient, False otherwise.
        """
        return amount <= self.balance
    
    def __str__(self):
        """
        Create a string representation of the category ledger.
        
        Returns:
            str: Formatted string showing all transactions and total.
        """
        # Create title line with asterisks, centered to 30 characters
        res = self.name.center(30, '*')
        res += '\n'
        
        # Add each ledger entry with formatted description and amount
        for l in self.ledger:
            # Description: max 23 characters, left-aligned
            res += f"{(l['description']+' '*23)[:23]}"
            
            # Amount: max 7 characters, right-aligned
            outp = f"{l['amount']:.2f}"
            while len(outp) < 7:
                outp = ' '+outp
            res += outp+'\n'
        
        # Add total line
        res += f'Total: {self.get_balance()}'
        return res


def create_spend_chart(categories):
    """
    Create a bar chart showing percentage spent by category.
    
    Args:
        categories (list): List of Category objects to include in chart.
    
    Returns:
        str: A string representation of the spending chart.
    """
    res = 'Percentage spent by category\n'
    percentages = []
    names = []
    all_spent = 0
    
    # Calculate total spent across all categories
    for c in categories:
        all_spent += c.spent
        percentages.append(c.spent)
        names.append(c.name)
    
    # Build each row of the chart (from 100% down to 0%)
    for i in range(100, -1, -10):
        # Format the percentage label (right-aligned, 3 chars + "|")
        out = f'{i}|'
        out = ' ' * (4-len(out)) + out
        
        # Handle case when no spending occurred
        if all_spent == 0:
            out += '   ' * len(categories)
        else:
            # Add "o" markers for each category based on their percentage
            for p in percentages:
                # Calculate percentage and round DOWN to nearest 10
                percentage = math.floor((p / all_spent) * 100 / 10) * 10
                if all_spent > 0 and percentage >= i:
                    out += ' o '
                else:
                    out += '   '
        res += out + ' \n'
    
    # Add horizontal line below the chart
    res += f"{' '*4}{'-'*3*len(categories)}-"

    # Add category names vertically below the chart
    j = 0
    while True:
        ou = f"\n{' '*4}"
        count = 0
        
        # Add one character from each category name
        for name in names:
            if j < len(name):
                ou += f' {name[j]} '
                count += 1
            else:
                ou += ' ' * 3
        
        # Break when all names have been fully printed
        if count == 0:
            break
        res += ou + ' '
        j += 1
    
    return res


# Main execution block for testing
if __name__ == '__main__':
    # Create Food category and add transactions
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    
    # Create other categories
    clothing = Category("Clothing")
    auto = Category("Auto")
    
    # Transfer funds from Food to other categories
    food.transfer(50, clothing)
    food.transfer(100, auto)
    
    # Make purchases in other categories
    clothing.withdraw(30.50, 't-shirt')
    auto.withdraw(70.30, "engine")

    # Display results
    print(food)
    print()
    print(create_spend_chart([food, clothing, auto]))
