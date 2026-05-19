import json
import os
from datetime import datetime
import uuid

# ==============================================================================
# EXPENSE TRACKER - Full Featured Terminal App
# Concepts used: Dictionaries, Lists, File I/O, Functions, Loops, Error Handling
# ==============================================================================

DATA_FILE = "expenses_data.json"

# Predefined categories (user can also add custom ones)
DEFAULT_CATEGORIES = [
    "🍔 Food",
    "🚌 Transport",
    "🏠 Bills",
    "🛍️  Shopping",
    "💊 Health",
    "🎬 Entertainment",
    "📚 Education",
    "💼 Other"
]


# ==============================================================================
# PART 1: FILE HANDLING - SAVING & LOADING DATA
# ==============================================================================

def load_data():
    """
    Loads expense data from JSON file.
    Data structure:
    {
        "expenses": [ {id, amount, category, description, date} ],
        "budgets":  { "Food": 5000, "Transport": 2000 }
    }
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    # Default structure if file doesn't exist
    return {"expenses": [], "budgets": {}}


def save_data(data):
    """Saves all expense data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)


# ==============================================================================
# PART 2: MENU DISPLAY
# ==============================================================================

def display_menu():
    print("\n" + "=" * 55)
    print("💰  EXPENSE TRACKER")
    print("=" * 55)
    print("1️⃣   Add Expense")
    print("2️⃣   View All Expenses")
    print("3️⃣   View by Category")
    print("4️⃣   Monthly Summary")
    print("5️⃣   Set / Update Budget Limits")
    print("6️⃣   Budget Overview (with chart)")
    print("7️⃣   Delete an Expense")
    print("8️⃣   Exit")
    print("=" * 55)


# ==============================================================================
# PART 3: ADD EXPENSE
# ==============================================================================

def add_expense(data):
    """
    Lets the user add a new expense.
    Asks for: amount, category, description
    Auto-fills: date, unique ID
    """
    print("\n📝 ADD NEW EXPENSE")
    print("-" * 40)

    # --- Get Amount ---
    while True:
        try:
            amount = float(input("💵 Enter amount (₹): ").strip())
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    # --- Choose Category ---
    print("\n📂 Choose a category:")
    for i, cat in enumerate(DEFAULT_CATEGORIES, 1):
        print(f"   {i}. {cat}")
    print(f"   {len(DEFAULT_CATEGORIES) + 1}. ➕ Add custom category")

    while True:
        try:
            cat_choice = int(input("\nEnter category number: "))
            if 1 <= cat_choice <= len(DEFAULT_CATEGORIES):
                category = DEFAULT_CATEGORIES[cat_choice - 1].split(" ", 1)[1].strip()
                break
            elif cat_choice == len(DEFAULT_CATEGORIES) + 1:
                category = input("✏️  Enter custom category name: ").strip()
                if category:
                    break
                print("❌ Category name cannot be empty.")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # --- Description ---
    description = input("📝 Description (optional, press Enter to skip): ").strip()
    if not description:
        description = "No description"

    # --- Create Expense Entry ---
    expense = {
        "id": str(uuid.uuid4())[:8],           # Short unique ID
        "amount": round(amount, 2),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "month": datetime.now().strftime("%Y-%m")  # For easy monthly filtering
    }

    data["expenses"].append(expense)
    save_data(data)

    print(f"\n✅ Expense of ₹{amount:.2f} added under '{category}'!")

    # --- Budget Warning ---
    _check_budget_warning(data, category)


def _check_budget_warning(data, category):
    """Checks if spending in a category exceeds the set budget and warns user."""
    if category not in data["budgets"]:
        return

    budget = data["budgets"][category]
    current_month = datetime.now().strftime("%Y-%m")

    # Sum all expenses in this category for the current month
    spent = sum(
        e["amount"] for e in data["expenses"]
        if e["category"] == category and e["month"] == current_month
    )

    percent = (spent / budget) * 100

    if percent >= 100:
        print(f"🚨 WARNING: You've EXCEEDED your ₹{budget:.0f} budget for '{category}'!")
        print(f"   Spent: ₹{spent:.2f} ({percent:.0f}% of budget)")
    elif percent >= 80:
        print(f"⚠️  HEADS UP: You've used {percent:.0f}% of your '{category}' budget.")
        print(f"   Spent: ₹{spent:.2f} / ₹{budget:.0f}")


# ==============================================================================
# PART 4: VIEW ALL EXPENSES
# ==============================================================================

def view_all_expenses(data):
    """Displays all expenses in a clean table format."""
    if not data["expenses"]:
        print("\n❌ No expenses recorded yet!")
        return

    print("\n" + "=" * 65)
    print("📋 ALL EXPENSES")
    print("=" * 65)
    print(f"{'ID':<10} {'Date':<12} {'Category':<16} {'Amount':>10}  Description")
    print("-" * 65)

    total = 0
    for e in sorted(data["expenses"], key=lambda x: x["date"], reverse=True):
        print(f"{e['id']:<10} {e['date']:<12} {e['category']:<16} ₹{e['amount']:>8.2f}  {e['description']}")
        total += e["amount"]

    print("-" * 65)
    print(f"{'TOTAL':<39} ₹{total:>8.2f}")
    print("=" * 65)


# ==============================================================================
# PART 5: VIEW BY CATEGORY
# ==============================================================================

def view_by_category(data):
    """Groups and displays expenses by category with subtotals."""
    if not data["expenses"]:
        print("\n❌ No expenses recorded yet!")
        return

    # Build a dictionary: { "Food": [expense1, expense2], ... }
    grouped = {}
    for e in data["expenses"]:
        cat = e["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(e)

    print("\n" + "=" * 55)
    print("📂 EXPENSES BY CATEGORY")
    print("=" * 55)

    grand_total = 0
    for category, expenses in grouped.items():
        subtotal = sum(e["amount"] for e in expenses)
        grand_total += subtotal

        print(f"\n📁 {category}  (₹{subtotal:.2f})")
        print(f"   {'Date':<12} {'Amount':>10}  Description")
        print(f"   {'-' * 40}")
        for e in sorted(expenses, key=lambda x: x["date"], reverse=True):
            print(f"   {e['date']:<12} ₹{e['amount']:>8.2f}  {e['description']}")

    print("\n" + "=" * 55)
    print(f"   GRAND TOTAL: ₹{grand_total:.2f}")
    print("=" * 55)


# ==============================================================================
# PART 6: MONTHLY SUMMARY
# ==============================================================================

def monthly_summary(data):
    """Shows a month-by-month breakdown with category-wise spending."""
    if not data["expenses"]:
        print("\n❌ No expenses recorded yet!")
        return

    # Group expenses by month
    months = {}
    for e in data["expenses"]:
        m = e["month"]
        if m not in months:
            months[m] = {}
        cat = e["category"]
        months[m][cat] = months[m].get(cat, 0) + e["amount"]

    print("\n" + "=" * 55)
    print("📅 MONTHLY SUMMARY")
    print("=" * 55)

    for month in sorted(months.keys(), reverse=True):
        cats = months[month]
        month_total = sum(cats.values())

        # Format month nicely: "2024-01" -> "January 2024"
        month_label = datetime.strptime(month, "%Y-%m").strftime("%B %Y")
        print(f"\n📆 {month_label}  —  Total: ₹{month_total:.2f}")
        print(f"   {'-' * 35}")

        # Sort categories by spending (highest first)
        for cat, amount in sorted(cats.items(), key=lambda x: x[1], reverse=True):
            # Mini bar chart: each █ = ₹500
            bars = int(amount // 500)
            bar = "█" * min(bars, 15)  # Cap at 15 bars for display
            print(f"   {cat:<16} ₹{amount:>8.2f}  {bar}")


# ==============================================================================
# PART 7: SET BUDGET LIMITS
# ==============================================================================

def set_budget(data):
    """Lets user set a monthly spending limit per category."""
    print("\n🎯 SET BUDGET LIMITS")
    print("-" * 40)
    print("Set how much you want to spend per category each month.\n")

    # Show all categories (from defaults + any already-tracked ones)
    all_cats = set(DEFAULT_CATEGORIES[i].split(" ", 1)[1].strip()
                   for i in range(len(DEFAULT_CATEGORIES) - 1))  # Exclude "Other"
    # Also add categories from actual expenses
    for e in data["expenses"]:
        all_cats.add(e["category"])

    cat_list = sorted(all_cats)
    for i, cat in enumerate(cat_list, 1):
        current = data["budgets"].get(cat, None)
        status = f"  (current: ₹{current:.0f})" if current else "  (not set)"
        print(f"  {i}. {cat}{status}")

    try:
        choice = int(input("\nEnter category number: ")) - 1
        if not (0 <= choice < len(cat_list)):
            print("❌ Invalid choice.")
            return

        category = cat_list[choice]
        amount = float(input(f"💰 Set monthly budget for '{category}' (₹): "))
        if amount <= 0:
            print("❌ Budget must be greater than 0.")
            return

        data["budgets"][category] = round(amount, 2)
        save_data(data)
        print(f"✅ Budget for '{category}' set to ₹{amount:.2f}/month!")

    except (ValueError, IndexError):
        print("❌ Invalid input.")


# ==============================================================================
# PART 8: BUDGET OVERVIEW WITH CHART
# ==============================================================================

def budget_overview(data):
    """
    Shows a visual bar chart of spending vs budget for current month.
    Uses █ for spent and ░ for remaining budget.
    """
    if not data["budgets"]:
        print("\n❌ No budgets set yet! Use option 5 to set budgets first.")
        return

    current_month = datetime.now().strftime("%Y-%m")
    month_label = datetime.now().strftime("%B %Y")

    print("\n" + "=" * 60)
    print(f"📊 BUDGET OVERVIEW — {month_label}")
    print("=" * 60)

    for category, budget in data["budgets"].items():
        # Calculate how much spent this month in this category
        spent = sum(
            e["amount"] for e in data["expenses"]
            if e["category"] == category and e["month"] == current_month
        )

        remaining = budget - spent
        percent = min((spent / budget) * 100, 100)  # Cap at 100%

        # Bar: 20 blocks total
        filled = int(percent / 5)   # Each block = 5%
        empty = 20 - filled

        # Color indicator based on usage
        if percent >= 100:
            indicator = "🚨"
        elif percent >= 80:
            indicator = "⚠️ "
        elif percent >= 50:
            indicator = "🟡"
        else:
            indicator = "✅"

        bar = "█" * filled + "░" * empty

        print(f"\n{indicator} {category}")
        print(f"   [{bar}] {percent:.0f}%")
        print(f"   Spent: ₹{spent:.2f} / Budget: ₹{budget:.2f}  |  Remaining: ₹{max(remaining, 0):.2f}")

    print("\n" + "=" * 60)


# ==============================================================================
# PART 9: DELETE AN EXPENSE
# ==============================================================================

def delete_expense(data):
    """Deletes an expense by its ID. Shows recent expenses first."""
    if not data["expenses"]:
        print("\n❌ No expenses to delete!")
        return

    print("\n🗑️  DELETE EXPENSE")
    print("-" * 50)

    # Show last 10 expenses
    recent = sorted(data["expenses"], key=lambda x: x["date"], reverse=True)[:10]
    print(f"{'#':<4} {'ID':<10} {'Date':<12} {'Category':<14} {'Amount':>9}")
    print("-" * 50)
    for i, e in enumerate(recent, 1):
        print(f"{i:<4} {e['id']:<10} {e['date']:<12} {e['category']:<14} ₹{e['amount']:>7.2f}")

    try:
        choice = int(input("\nEnter # to delete (or 0 to cancel): "))
        if choice == 0:
            print("❌ Cancelled.")
            return

        expense = recent[choice - 1]
        confirm = input(f"Are you sure you want to delete ₹{expense['amount']:.2f} ({expense['description']})? (yes/no): ").strip().lower()

        if confirm == "yes":
            data["expenses"] = [e for e in data["expenses"] if e["id"] != expense["id"]]
            save_data(data)
            print(f"✅ Expense deleted successfully!")
        else:
            print("❌ Cancelled.")

    except (ValueError, IndexError):
        print("❌ Invalid selection.")


# ==============================================================================
# PART 10: MAIN PROGRAM LOOP
# ==============================================================================

def main():
    print("💰 Welcome to Expense Tracker!")
    print("   Track your spending. Set budgets. Stay in control.")

    while True:
        data = load_data()
        display_menu()

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_all_expenses(data)
        elif choice == "3":
            view_by_category(data)
        elif choice == "4":
            monthly_summary(data)
        elif choice == "5":
            set_budget(data)
        elif choice == "6":
            budget_overview(data)
        elif choice == "7":
            delete_expense(data)
        elif choice == "8":
            print("\n👋 Keep tracking those expenses! Goodbye! 💪")
            break
        else:
            print("❌ Invalid choice! Please enter 1-8.")


if __name__ == "__main__":
    main()
