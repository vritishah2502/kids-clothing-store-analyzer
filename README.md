# ABC Kids Clothing Store – Billing & Store Analysis

## About the Project

This is a beginner Python project based on a kids' clothing store.

The project has two parts:

1. **Billing System** – collects customer and product information, calculates the subtotal, applies discounts, and generates the final bill.
2. **Store Analysis** – analyzes the entered product data to provide basic store insights.

## Features

### Billing System

* Collects customer information:

  * Name
  * Age
  * City
  * Phone Number

* Allows the user to enter multiple products.

* Stores product information using dictionaries.

* Calculates the subtotal based on price and quantity.

* Applies discounts based on the subtotal:

  * Below ₹2,000 → No discount
  * ₹2,000–₹4,999 → 3%
  * ₹5,000–₹9,999 → 7%
  * ₹10,000–₹49,999 → 12%
  * ₹50,000 and above → 20%

* Calculates discount amount.

* Calculates final amount.

* Displays the amount saved.

### Store Analysis

The analysis module provides:

* Total units sold
* Most expensive product
* Category-wise units sold for:

  * Female
  * Male
  * Unisex

## Python Concepts Used

This project helped me practice:

* Variables
* Data types
* Strings
* Integers and floats
* Dictionaries
* Lists
* `input()` and `print()`
* `if`, `elif`, and `else`
* `for` and `while` loops
* Functions
* `return`
* Dictionary `.get()` method
* Dictionary updating
* Basic calculations
* Importing data from another Python file
* Working with multiple Python files

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run `billingsystem.py`.
5. Enter the customer and product information when prompted.
6. After entering the products, run `store_analysis.py` to view the store analysis.

## Important Note

For the store analysis to work correctly, use one of the following categories when entering products:

* `Female`
* `Male`
* `Unisex`

## What I Learned

Through this project, I learned how to work with lists and dictionaries, use loops and conditional statements, create functions, return values from functions, and use data from one Python file in another.

This project was created as a learning project while practicing Python fundamentals.
