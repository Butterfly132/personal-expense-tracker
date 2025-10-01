💰 Personal Expense Tracker
A simple yet powerful command-line expense tracking application built with Python. Track your daily expenses, categorize them, and generate weekly or monthly summaries to better manage your finances.
✨ Features

Easy Expense Entry: Quickly add expenses with category, amount, description, and date
Multiple Categories: Pre-defined categories including Food, Rent, Travel, Entertainment, Utilities, Healthcare, Shopping, and Other
Weekly & Monthly Summaries: Generate comprehensive reports showing spending by category
Detailed Analytics: View percentage breakdowns, total expenses, and highest spending categories
Complete Expense History: View all recorded expenses in a chronological list
User-Friendly Interface: Clean, interactive command-line interface

📋 Requirements

Python 3.6 or higher
No external dependencies required (uses only Python standard library)

🚀 Installation

Clone the repository:

bashgit clone https://github.com/Butterfly132/personal-expense-tracker.git
cd personal-expense-tracker

Run the application:

bashpython expense_tracker.py
💻 Usage
Main Menu Options
When you run the application, you'll see the following menu:
--- Main Menu ---
1. Add Expense
2. View Weekly Summary
3. View Monthly Summary
4. View All Expenses
5. Exit
Adding an Expense

Select option 1 from the main menu
Choose a category (1-8)
Enter the amount (e.g., 25.50)
Add an optional description
Enter a date (DD-MM-YYYY format) or press Enter for today's date

Viewing Summaries
Weekly Summary (Option 2):

Shows all expenses from the last 7 days
Breaks down spending by category with percentages
Displays total spent and average per expense

Monthly Summary (Option 3):

Shows all expenses from the last 30 days
Provides the same detailed breakdown as weekly summary

Example Summary Output:
==================================================
Monthly Expense Summary
Period: 01-09-2025 to 01-10-2025
==================================================

Category                     Amount   Percentage
--------------------------------------------------
Food                        $450.00       45.0%
Rent                        $300.00       30.0%
Travel                      $150.00       15.0%
Entertainment               $100.00       10.0%
--------------------------------------------------
TOTAL                      $1000.00      100.0%
==================================================

Total Expenses: 12
Average per expense: $83.33
Highest category: Food ($450.00)
📊 Categories
The tracker includes the following expense categories:

🍔 Food: Groceries, restaurants, takeout
🏠 Rent: Monthly rent payments
✈️ Travel: Transportation, fuel, tickets
🎬 Entertainment: Movies, games, hobbies
💡 Utilities: Electricity, water, internet
🏥 Healthcare: Medical expenses, pharmacy
🛍️ Shopping: Clothing, electronics, misc purchases
📦 Other: Any other expenses

🔧 Features in Detail
Date Flexibility

Enter custom dates for past expenses
Default to today's date for quick entry
Format: DD-MM-YYYY (e.g., 15-09-2025)

Smart Summaries

Automatic calculation of percentage breakdowns
Identifies highest spending categories
Provides average expense calculations

Data Persistence

All expenses are stored in memory during the session
Easy to extend with file-based or database storage

🛠️ Future Enhancements
Potential features for future versions:

 Save expenses to file (JSON/CSV)
 Load previous expense data
 Custom date range queries
 Budget setting and alerts
 Export reports to PDF
 Data visualization with charts
 Multi-currency support
 Recurring expense tracking

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository
Create a new branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
👤 Author
Ishita Singh

GitHub: @Butterfly132

🙏 Acknowledgments

Built with Python's standard library
Inspired by the need for simple personal finance management

📧 Contact
Have questions or suggestions? Feel free to open an issue or contact me directly!

⭐ If you find this project useful, please consider giving it a star on GitHub!
