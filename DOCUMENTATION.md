# Personal Expense Tracker - Project Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Planning Phase](#planning-phase)
3. [Development Process](#development-process)
4. [Code Structure](#code-structure)
5. [Testing Process](#testing-process)
6. [GitHub Deployment](#github-deployment)
7. [Challenges Faced](#challenges-faced)
8. [Future Improvements](#future-improvements)
9. [Conclusion](#conclusion)

---

## 1. Project Overview

### 1.1 Project Name
Personal Expense Tracker

### 1.2 Purpose
To create a simple command-line application that helps users track their daily expenses, categorize them, and generate weekly or monthly financial summaries.

### 1.3 Technology Stack
- **Programming Language**: Python 3.x
- **Libraries Used**: 
  - `datetime` - For date and time handling
  - `timedelta` - For calculating date ranges
  - `collections.defaultdict` - For efficient category totals calculation

### 1.4 Project Goals
- Create an intuitive user interface for expense entry
- Provide multiple expense categories
- Generate weekly and monthly expense reports
- Calculate statistics like totals, percentages, and averages
- Maintain a complete expense history

---

## 2. Planning Phase

### 2.1 Requirements Analysis

**Functional Requirements:**
- User can add expenses with category, amount, description, and date
- User can view weekly summary (last 7 days)
- User can view monthly summary (last 30 days)
- User can view all recorded expenses
- System should calculate totals by category
- System should show percentage breakdown
- System should identify highest spending category

**Non-Functional Requirements:**
- Easy to use command-line interface
- Fast response time
- Clear and readable output formatting
- Input validation for amounts and dates

### 2.2 Design Decisions

**Architecture:**
- Object-Oriented Programming approach using a single `ExpenseTracker` class
- In-memory storage for simplicity (can be extended to file/database storage)

**Data Structure:**
- Expenses stored as list of dictionaries
- Each expense contains: category, amount, description, date

**Categories Chosen:**
1. Food
2. Rent
3. Travel
4. Entertainment
5. Utilities
6. Healthcare
7. Shopping
8. Other

---

## 3. Development Process

### 3.1 Step 1: Setting Up the Environment

**Date Started**: [Add your date]

**Actions Taken:**
1. Installed Python 3.x on the system
2. Created project directory: `personal-expense-tracker`
3. Created main file: `expense_tracker.py`

**Commands Used:**
```bash
mkdir personal-expense-tracker
cd personal-expense-tracker
touch expense_tracker.py  # or create file manually
```

### 3.2 Step 2: Implementing Core Class Structure

**Approach:**
Created the `ExpenseTracker` class with initialization method.

**Code Implementation:**
```python
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ['Food', 'Rent', 'Travel', 'Entertainment', 
                          'Utilities', 'Healthcare', 'Shopping', 'Other']
```

**Reasoning:**
- Used a list to store expenses for easy iteration and filtering
- Pre-defined categories for consistency and user convenience

### 3.3 Step 3: Implementing Add Expense Functionality

**Features Implemented:**
- Category selection with numbered menu
- Amount input with validation (must be positive)
- Optional description field
- Date input with default to today's date
- Input validation and error handling

**Key Code Sections:**
```python
def add_expense(self):
    # Display categories
    # Get user input with validation
    # Create expense dictionary
    # Add to expenses list
```

**Challenges:**
- Ensuring proper input validation for numeric values
- Handling invalid date formats gracefully
- Providing clear error messages

### 3.4 Step 4: Implementing Summary Reports

**Weekly Summary Implementation:**
- Filters expenses from last 7 days
- Groups by category and calculates totals
- Displays formatted table with percentages

**Monthly Summary Implementation:**
- Filters expenses from last 30 days
- Same calculation logic as weekly summary

**Key Features:**
- Dynamic date range calculation using `timedelta`
- Percentage calculation: `(category_total / overall_total) * 100`
- Formatted output with proper alignment

**Code Logic:**
```python
def get_summary(self, period='monthly'):
    # Calculate date range
    # Filter expenses by date
    # Group by category using defaultdict
    # Calculate totals and percentages
    # Display formatted table
```

### 3.5 Step 5: Implementing View All Expenses

**Features:**
- Lists all expenses in reverse chronological order (newest first)
- Displays date, category, amount, and description
- Formatted table output with proper column alignment

### 3.6 Step 6: Creating Main Menu Loop

**Implementation:**
- Infinite loop for continuous operation
- Menu-driven interface with 5 options
- Input validation for menu choices
- Clean exit functionality

---

## 4. Code Structure

### 4.1 Class Methods Overview

| Method | Purpose | Input | Output |
|--------|---------|-------|--------|
| `__init__()` | Initialize tracker | None | None |
| `add_expense()` | Add new expense | User input | Confirmation message |
| `get_summary()` | Generate report | period (weekly/monthly) | Formatted summary |
| `view_all_expenses()` | List all expenses | None | Formatted table |
| `run()` | Main program loop | User menu choices | Interactive session |

### 4.2 Data Flow

```
User Input → Input Validation → Data Storage (List)
                                      ↓
                            Filtering & Processing
                                      ↓
                            Calculation & Analysis
                                      ↓
                            Formatted Output Display
```

### 4.3 File Structure

```
personal-expense-tracker/
├── expense_tracker.py    # Main application code
├── README.md            # Project documentation and usage guide
└── .gitignore          # Git ignore file (optional)
```

---

## 5. Testing Process

### 5.1 Test Cases Executed

**Test Case 1: Adding an Expense**
- **Input**: Category: Food, Amount: 50, Description: "Groceries", Date: Today
- **Expected**: Expense added successfully
- **Result**: ✅ Passed

**Test Case 2: Invalid Amount Input**
- **Input**: Amount: -10
- **Expected**: Error message, prompt to re-enter
- **Result**: ✅ Passed

**Test Case 3: Invalid Date Format**
- **Input**: Date: "2024/09/15" (wrong format)
- **Expected**: Error message, defaults to today
- **Result**: ✅ Passed

**Test Case 4: Weekly Summary with No Data**
- **Input**: Request weekly summary with empty expense list
- **Expected**: "No expenses recorded yet!" message
- **Result**: ✅ Passed

**Test Case 5: Monthly Summary Calculation**
- **Input**: 10 expenses across different categories
- **Expected**: Correct totals, percentages sum to 100%
- **Result**: ✅ Passed

**Test Case 6: View All Expenses**
- **Input**: Request to view all expenses
- **Expected**: Chronological list with proper formatting
- **Result**: ✅ Passed

### 5.2 Edge Cases Tested

1. **Empty expense list**: All views handle gracefully
2. **Single expense**: Calculations work correctly (100% in one category)
3. **Very large amounts**: No overflow or formatting issues
4. **Special characters in description**: Handled properly
5. **Future dates**: Accepted (user might log planned expenses)

---

## 6. GitHub Deployment

### 6.1 Git Installation

**Date**: [Add your date]

**Steps Taken:**
1. Downloaded Git from git-scm.com
2. Installed with default settings
3. Verified installation: `git --version`

**Output:**
```
git version 2.39.0
```

### 6.2 Git Configuration

**Commands Executed:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Verification:**
```bash
git config --list
```

### 6.3 Repository Initialization

**Steps:**
1. Navigated to project directory
2. Initialized Git repository
3. Added files to staging
4. Made initial commit

**Commands:**
```bash
cd personal-expense-tracker
git init
git add .
git commit -m "Initial commit: Personal Expense Tracker"
```

**Output:**
```
Initialized empty Git repository in /path/to/personal-expense-tracker/.git/
[main (root-commit) abc1234] Initial commit: Personal Expense Tracker
 2 files changed, 250 insertions(+)
 create mode 100644 README.md
 create mode 100644 expense_tracker.py
```

### 6.4 GitHub Repository Creation

**Steps:**
1. Logged into GitHub account
2. Clicked "New Repository"
3. Repository name: `personal-expense-tracker`
4. Description: "A Python command-line expense tracker"
5. Visibility: Public
6. Created repository

### 6.5 Pushing to GitHub

**Commands:**
```bash
git branch -M main
git remote add origin https://github.com/username/personal-expense-tracker.git
git push -u origin main
```

**Result:**
Successfully pushed code to GitHub. Repository is now live at:
`https://github.com/username/personal-expense-tracker`

### 6.6 Repository Contents

**Files in Repository:**
1. `expense_tracker.py` - Main application code (250 lines)
2. `README.md` - Project documentation and usage guide

---

## 7. Challenges Faced

### 7.1 Challenge 1: Date Handling
**Problem**: Needed to calculate date ranges for weekly/monthly summaries

**Solution**: Used `datetime` and `timedelta` modules
```python
start_date = now - timedelta(days=7)  # For weekly
```

**Learning**: Python's datetime module is powerful for date arithmetic

### 7.2 Challenge 2: Input Validation
**Problem**: Users might enter invalid data (negative amounts, wrong date formats)

**Solution**: Implemented try-except blocks with while loops for validation
```python
while True:
    try:
        amount = float(input("Enter amount: $"))
        if amount > 0:
            break
    except ValueError:
        print("Please enter a valid number.")
```

**Learning**: Robust input validation improves user experience

### 7.3 Challenge 3: Formatting Output
**Problem**: Needed clean, aligned table output for summaries

**Solution**: Used f-strings with width specifiers
```python
print(f"{category:<20} ${amount:>14.2f} {percentage:>11.1f}%")
```

**Learning**: Python f-strings offer powerful formatting capabilities

### 7.4 Challenge 4: GitHub Authentication
**Problem**: Initial push to GitHub required authentication

**Solution**: Used Personal Access Token instead of password

**Learning**: GitHub now requires tokens for command-line access

---

## 8. Future Improvements

### 8.1 Planned Features

**Version 2.0:**
- [ ] File-based persistence (JSON/CSV)
- [ ] Load previous expense data on startup
- [ ] Edit/delete existing expenses
- [ ] Custom date range queries

**Version 3.0:**
- [ ] Budget setting and alerts
- [ ] Recurring expense tracking
- [ ] Export reports to PDF
- [ ] Data visualization with charts
- [ ] Multi-currency support

### 8.2 Technical Improvements

- [ ] Add unit tests using pytest
- [ ] Implement database storage (SQLite)
- [ ] Create GUI version using Tkinter
- [ ] Add configuration file for customization
- [ ] Implement data backup functionality

### 8.3 Code Optimization

- [ ] Refactor summary generation into separate methods
- [ ] Add type hints for better code documentation
- [ ] Implement logging for debugging
- [ ] Optimize date filtering performance for large datasets

---

## 9. Conclusion

### 9.1 Project Summary

Successfully developed a functional Personal Expense Tracker application that meets all initial requirements. The application provides an intuitive command-line interface for tracking expenses with comprehensive reporting capabilities.

### 9.2 Key Achievements

✅ Implemented core expense tracking functionality  
✅ Created weekly and monthly summary reports  
✅ Added input validation and error handling  
✅ Designed clean, user-friendly interface  
✅ Documented code and usage instructions  
✅ Deployed to GitHub for version control  

### 9.3 Skills Developed

- **Python Programming**: Classes, data structures, datetime handling
- **Software Design**: Object-oriented programming principles
- **Version Control**: Git and GitHub workflow
- **Documentation**: Technical writing and README creation
- **Testing**: Manual testing and edge case identification
- **Problem Solving**: Input validation and error handling

### 9.4 Time Investment

- **Planning**: 2 hours
- **Development**: 4 hours
- **Testing**: 1 hour
- **Documentation**: 2 hours
- **GitHub Setup**: 1 hour
- **Total**: ~10 hours

### 9.5 Lessons Learned

1. **Planning is crucial**: Defining requirements upfront saved development time
2. **User input is unpredictable**: Always validate and handle errors
3. **Documentation matters**: Good README helps users understand the project
4. **Version control is essential**: Git makes collaboration and tracking changes easy
5. **Iterative development works**: Starting simple and adding features gradually is effective

### 9.6 Personal Reflection

This project provided hands-on experience with Python development, from initial concept to deployment. The most valuable learning was understanding how to structure a complete application with proper error handling and user experience considerations.

---

## 📊 Project Statistics

- **Lines of Code**: ~250
- **Number of Functions**: 5
- **Number of Categories**: 8
- **Testing Time**: 1 hour
- **GitHub Stars**: [Update as project gains popularity]
- **Contributors**: 1

---

## 📞 Contact Information

**Developer**: Ishia Singh  
**Email**: singhishita5242@gmail.com  
**GitHub**:   https://github.com/Butterfly132
**Project Repository**: https://github.com/Butterfly/personal-expense-tracker

---

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated**: [Current Date]  
**Version**: 1.0.0