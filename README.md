# 💰 Budget Manager & Visualizer

A robust, Object-Oriented Python application designed to manage budget categories, track ledger transactions, and visualize spending habits via a dynamically generated bar chart.

## 🚀 Project Overview

This project implements a budget management system that allows users to create distinct categories (e.g., Food, Clothing, Auto). It handles financial transactions with logic to prevent overdrafts and facilitates transfers between categories. Additionally, it features a custom algorithmic engine to render a percentage-based spending chart within the terminal.

## 🛠 Software Engineering Skills Highlighted

This project demonstrates several key software engineering and programming competencies:

### 1. Object-Oriented Design (OOP) & Encapsulation
- **Class Architecture:** Utilized a `Category` class to encapsulate data (`ledger`, `balance`) and behaviors (`deposit`, `withdraw`, `transfer`).
- **State Management:** Maintained internal state integrity through methods like `get_balance()` and `check_funds()`, ensuring the object controls its own data modification rules.
- **Polymorphism:** Overrode the `__str__` dunder method to provide a human-readable, formatted string representation of the object state (the ledger), acting as a view layer for the data.

### 2. Algorithmic Logic & Data Transformation
- **Data Visualization Logic:** The `create_spend_chart` function contains complex logic to transform raw numerical data into a visual bar chart representation.
- **Normalization:** Implemented mathematical logic (`math.floor`) to normalize spending data into rounded percentages (nearest 10) for charting.
- **Matrix Traversal:** The vertical printing of category names requires a nested loop structure that effectively pivots the string data (transposing rows to columns) to handle varying string lengths dynamically.

### 3. Defensive Programming
- **Guard Clauses:** The `withdraw` and `transfer` methods utilize the `check_funds` helper method as a guard clause. This prevents operations that would result in a negative balance, ensuring data integrity.
- **Return Value Logic:** Boolean return values are used to indicate transaction success or failure, allowing the calling code to handle errors gracefully.

### 4. Advanced String Manipulation
- **Formatting:** Extensive use of f-strings, slicing, and alignment methods (`.center()`, `.ljust()`, `.rjust()`) to create a strict tabular format for the ledger and the chart.
- **Dynamic Padding:** Logic to calculate whitespace dynamically ensures the UI remains consistent regardless of the length of the numbers or descriptions.

---

## 💻 Usage

### Quick Start
No external dependencies are required. This script runs on standard Python 3.
