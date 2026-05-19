# 💰 Expense Tracker

> A full-featured terminal-based expense tracking app built in Python. Track your spending, set budgets, and view monthly summaries — all from your command line!

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Beginner Friendly](https://img.shields.io/badge/level-beginner-brightgreen.svg)]()
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

---

## 🎯 Features

- ✅ **Add Expenses** — Log amount, category, and description
- ✅ **Predefined Categories** — Food, Transport, Bills, Shopping, Health, and more
- ✅ **Custom Categories** — Add your own category on the fly
- ✅ **Budget Limits** — Set monthly spending limits per category
- ✅ **Budget Warnings** — Get alerted at 80% and 100% of your budget
- ✅ **Visual Bar Charts** — See spending vs budget with █░ progress bars
- ✅ **Monthly Summary** — Month-by-month breakdown with category totals
- ✅ **View by Category** — Grouped expense view with subtotals
- ✅ **Delete Expenses** — Remove entries safely with confirmation
- ✅ **Persistent Data** — All data saved automatically to a JSON file

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- A terminal / command prompt
- That's it — no libraries to install!

### Run the App

1. **Download or clone the project**
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

2. **Run the program**
```bash
python expense_tracker.py
```

> If that doesn't work, try:
```bash
python3 expense_tracker.py
```

---

## 📖 Usage

When you run the program, you'll see:

```
💰 Welcome to Expense Tracker!
   Track your spending. Set budgets. Stay in control.

=======================================================
💰  EXPENSE TRACKER
=======================================================
1️⃣   Add Expense
2️⃣   View All Expenses
3️⃣   View by Category
4️⃣   Monthly Summary
5️⃣   Set / Update Budget Limits
6️⃣   Budget Overview (with chart)
7️⃣   Delete an Expense
8️⃣   Exit
=======================================================
```

### Example Workflow

```bash
# Add an expense
Choose an option (1-8): 1
💵 Enter amount (₹): 250
📂 Choose a category: 1 (Food)
📝 Description: Lunch at cafe
✅ Expense of ₹250.00 added under 'Food'!

# View budget overview
Choose an option (1-8): 6

📊 BUDGET OVERVIEW — May 2026
✅ Food
   [████████░░░░░░░░░░░░] 40%
   Spent: ₹2000.00 / Budget: ₹5000.00  |  Remaining: ₹3000.00

⚠️  Transport
   [████████████████░░░░] 80%
   Spent: ₹1600.00 / Budget: ₹2000.00  |  Remaining: ₹400.00
```

---

## 📁 Project Structure

```
expense-tracker/
│
├── expense_tracker.py     # Main application
├── expenses_data.json     # Auto-created data file
└── README.md              # This file
```

---

## 💾 Data Structure

All data is saved in `expenses_data.json`:

```json
{
  "expenses": [
    {
      "id": "a1b2c3d4",
      "amount": 250.00,
      "category": "Food",
      "description": "Lunch at cafe",
      "date": "2026-05-19",
      "month": "2026-05"
    }
  ],
  "budgets": {
    "Food": 5000.00,
    "Transport": 2000.00
  }
}
```

---

## 🎓 Python Concepts Used

| Concept | Where It's Used |
|---|---|
| Dictionaries | Storing expenses and budgets |
| Lists | Expense records |
| File I/O | Loading/saving JSON data |
| Functions | Each menu option is a function |
| Loops | Menu loop, displaying expenses |
| Error Handling | `try/except` for invalid inputs |
| f-strings | Formatted output |
| `uuid` | Unique expense IDs |
| `datetime` | Auto-filling dates, monthly filters |
| List comprehensions | Filtering expenses by category/month |

---

## 🔧 Customization Ideas

### Beginner
- Add more default categories
- Change the currency symbol from ₹ to $ or €
- Add a "search by description" feature

### Intermediate
- Export expenses to a `.csv` file (open in Excel)
- Add a yearly summary view
- Show the top 3 spending categories

### Advanced
- Build a Flask web version with charts
- Add user login support
- Sync data to Google Sheets

---

## ❓ FAQ

**Q: Where is my data stored?**  
A: In `expenses_data.json` in the same folder as the script. It's created automatically on first run.

**Q: How do I reset all data?**  
A: Delete the `expenses_data.json` file and restart the program.

**Q: Can I use this on Windows, Mac, and Linux?**  
A: Yes! Works on all platforms with Python 3.7+.

**Q: Do I need to install any libraries?**  
A: No! Only built-in Python libraries are used (`json`, `os`, `datetime`, `uuid`).

**Q: The emojis look broken on my terminal.**  
A: On Windows, open the terminal and run `chcp 65001` before running the script, or use Windows Terminal instead of Command Prompt.

---

## 📊 Learning Path

```
Python Basics (Variables, Loops)
           ↓
    Habit Tracker
           ↓
  THIS PROJECT ← You are here
           ↓
  Flask Web Version
           ↓
  Database + Full Stack
```

---

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ for Python learners**

⭐ If this helped you, give it a star on GitHub!
