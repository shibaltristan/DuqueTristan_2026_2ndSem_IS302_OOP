# Inventory Management System

A simple object-oriented inventory management system built in Python for the Week 12 final practical exam.

## Description
This system allows a small store owner to add products, view all products, search for a product by ID, and update product quantities. Product data is stored in a text file using basic file handling.

## Features
- Add new products
- View all products
- Search for a product by ID
- Update product quantity
- Menu-driven user interface
- Input validation with exception handling
- Encapsulated `Product` class

## Files
- `main.py` — program entry point and menu logic
- `product.py` — `Product` class with private attributes
- `inventory_manager.py` — file-based product storage and retrieval functions
- `products.txt` — inventory data file
- `README.md` — project documentation

## How to run the program
1. Open a command prompt in the `week12_final_exam` folder.
2. Run `python main.py`.

## Example output
```
INVENTORY MANAGEMENT SYSTEM
1 Add Product
2 View Products
3 Search Product
4 Update Quantity
5 Exit
Enter choice: 1
Enter Product ID: P001
Enter Product Name: Laptop
Enter Price: 45000
Enter Quantity: 10
Product added successfully
```
