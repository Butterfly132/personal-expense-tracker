from datetime import datetime, timedelta
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ['Food', 'Rent', 'Travel', 'Entertainment', 'Utilities', 'Healthcare', 'Shopping', 'Other']
    
    def add_expense(self):
        print("\n--- Add New Expense ---")
        
        # Display categories
        print("\nCategories:")
        for i, cat in enumerate(self.categories, 1):
            print(f"{i}. {cat}")
        
        # Get category
        while True:
            try:
                cat_choice = int(input("\nSelect category (1-{}): ".format(len(self.categories))))
                if 1 <= cat_choice <= len(self.categories):
                    category = self.categories[cat_choice - 1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount: $"))
                if amount > 0:
                    break
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get description
        description = input("Enter description (optional): ").strip()
        
        # Get date
        date_input = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
        if date_input:
            try:
                date = datetime.strptime(date_input, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.now()
        else:
            date = datetime.now()
        
        # Add expense
        expense = {
            'category': category,
            'amount': amount,
            'description': description,
            'date': date
        }
        self.expenses.append(expense)
        print(f"\n✓ Expense added successfully! ${amount:.2f} for {category}")
    
    def get_summary(self, period='monthly'):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        
        now = datetime.now()
        
        if period == 'weekly':
            start_date = now - timedelta(days=7)
            period_name = "Weekly"
        else:  # monthly
            start_date = now - timedelta(days=30)
            period_name = "Monthly"
        
        # Filter expenses by period
        period_expenses = [e for e in self.expenses if e['date'] >= start_date]
        
        if not period_expenses:
            print(f"\nNo expenses in the last {period_name.lower()} period!")
            return
        
        # Calculate totals by category
        category_totals = defaultdict(float)
        total = 0
        
        for expense in period_expenses:
            category_totals[expense['category']] += expense['amount']
            total += expense['amount']
        
        # Display summary
        print(f"\n{'='*50}")
        print(f"{period_name} Expense Summary")
        print(f"Period: {start_date.strftime('%d-%m-%Y')} to {now.strftime('%d-%m-%Y')}")
        print(f"{'='*50}")
        
        print(f"\n{'Category':<20} {'Amount':>15} {'Percentage':>12}")
        print("-" * 50)
        
        for category in sorted(category_totals.keys()):
            amount = category_totals[category]
            percentage = (amount / total) * 100
            print(f"{category:<20} ${amount:>14.2f} {percentage:>11.1f}%")
        
        print("-" * 50)
        print(f"{'TOTAL':<20} ${total:>14.2f} {100.0:>11.1f}%")
        print(f"{'='*50}\n")
        
        # Additional stats
        print(f"Total Expenses: {len(period_expenses)}")
        print(f"Average per expense: ${total/len(period_expenses):.2f}")
        print(f"Highest category: {max(category_totals, key=category_totals.get)} (${category_totals[max(category_totals, key=category_totals.get)]:.2f})")
    
    def view_all_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        
        print(f"\n{'='*70}")
        print("All Expenses")
        print(f"{'='*70}")
        print(f"{'Date':<12} {'Category':<15} {'Amount':>10} {'Description':<30}")
        print("-" * 70)
        
        for expense in sorted(self.expenses, key=lambda x: x['date'], reverse=True):
            date_str = expense['date'].strftime('%d-%m-%Y')
            desc = expense['description'][:27] + "..." if len(expense['description']) > 30 else expense['description']
            print(f"{date_str:<12} {expense['category']:<15} ${expense['amount']:>9.2f} {desc:<30}")
        
        print(f"{'='*70}\n")
    
    def run(self):
        print("\n" + "="*50)
        print("     PERSONAL EXPENSE TRACKER")
        print("="*50)
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Expense")
            print("2. View Weekly Summary")
            print("3. View Monthly Summary")
            print("4. View All Expenses")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.get_summary('weekly')
            elif choice == '3':
                self.get_summary('monthly')
            elif choice == '4':
                self.view_all_expenses()
            elif choice == '5':
                print("\nThank you for using Expense Tracker! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

# Run the tracker
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
