import csv
import os
from datetime import datetime
import uuid

class InventoryManager:
    def __init__(self):
        self.inventory_file = "data/inventory.csv"
        self.transactions_file = "data/transactions.csv"
        self.init_data_files()
    
    def init_data_files(self):
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Initialize inventory file
        if not os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['product_id', 'name', 'quantity', 'price', 'category', 'reorder_level'])
        
        # Initialize transactions file
        if not os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['transaction_id', 'product_id', 'type', 'quantity', 'date', 'notes'])
    
    def add_product(self, name, quantity, price, category, reorder_level):
        product_id = str(uuid.uuid4())[:8]
        with open(self.inventory_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([product_id, name, quantity, price, category, reorder_level])
        return product_id
    
    def update_quantity(self, product_id, change_amount, transaction_type, notes=""):
        updated_inventory = []
        product_found = False
        
        # Update inventory
        with open(self.inventory_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['product_id'] == product_id:
                    product_found = True
                    new_quantity = int(row['quantity']) + change_amount
                    if new_quantity < 0:
                        raise ValueError("Insufficient inventory")
                    row['quantity'] = str(new_quantity)
                updated_inventory.append(row)
        
        if not product_found:
            raise ValueError("Product not found")
        
        # Write updated inventory
        with open(self.inventory_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['product_id', 'name', 'quantity', 'price', 'category', 'reorder_level'])
            writer.writeheader()
            writer.writerows(updated_inventory)
        
        # Record transaction
        transaction_id = str(uuid.uuid4())
        with open(self.transactions_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([transaction_id, product_id, transaction_type, change_amount, datetime.now(), notes])
    
    def get_low_stock_items(self):
        low_stock = []
        with open(self.inventory_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['quantity']) <= int(row['reorder_level']):
                    low_stock.append(row)
        return low_stock
    
    def get_inventory_report(self):
        with open(self.inventory_file, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    def get_transaction_history(self, product_id=None):
        transactions = []
        with open(self.transactions_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if product_id is None or row['product_id'] == product_id:
                    transactions.append(row)
        return transactions

def display_menu():
    print("\n=== Inventory Management System ===")
    print("1. Add New Product")
    print("2. Record Stock In")
    print("3. Record Stock Out")
    print("4. View Inventory Report")
    print("5. View Low Stock Alert")
    print("6. View Transaction History")
    print("7. Exit")
    return input("Choose an option (1-7): ")

def main():
    manager = InventoryManager()
    
    while True:
        choice = display_menu()
        
        try:
            if choice == "1":
                name = input("Enter product name: ")
                quantity = int(input("Enter initial quantity: "))
                price = float(input("Enter unit price: "))
                category = input("Enter category: ")
                reorder_level = int(input("Enter reorder level: "))
                
                product_id = manager.add_product(name, quantity, price, category, reorder_level)
                print(f"Product added successfully! Product ID: {product_id}")
            
            elif choice == "2":
                product_id = input("Enter product ID: ")
                quantity = int(input("Enter quantity to add: "))
                notes = input("Enter notes (optional): ")
                manager.update_quantity(product_id, quantity, "IN", notes)
                print("Stock added successfully!")
            
            elif choice == "3":
                product_id = input("Enter product ID: ")
                quantity = int(input("Enter quantity to remove: "))
                notes = input("Enter notes (optional): ")
                manager.update_quantity(product_id, -quantity, "OUT", notes)
                print("Stock removed successfully!")
            
            elif choice == "4":
                inventory = manager.get_inventory_report()
                print("\nCurrent Inventory:")
                print("-" * 80)
                print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Category':<15} {'Reorder Level':<10}")
                print("-" * 80)
                for item in inventory:
                    print(f"{item['product_id']:<10} {item['name']:<20} {item['quantity']:<10} "
                          f"${item['price']:<9} {item['category']:<15} {item['reorder_level']:<10}")
            
            elif choice == "5":
                low_stock = manager.get_low_stock_items()
                print("\nLow Stock Alert:")
                print("-" * 80)
                for item in low_stock:
                    print(f"Product: {item['name']} (ID: {item['product_id']})")
                    print(f"Current Quantity: {item['quantity']}, Reorder Level: {item['reorder_level']}")
                    print("-" * 40)
            
            elif choice == "6":
                product_id = input("Enter product ID (press Enter for all transactions): ").strip()
                transactions = manager.get_transaction_history(product_id if product_id else None)
                print("\nTransaction History:")
                print("-" * 100)
                for trans in transactions:
                    print(f"ID: {trans['transaction_id']}")
                    print(f"Product ID: {trans['product_id']}")
                    print(f"Type: {trans['type']}, Quantity: {trans['quantity']}")
                    print(f"Date: {trans['date']}")
                    if trans['notes']:
                        print(f"Notes: {trans['notes']}")
                    print("-" * 50)
            
            elif choice == "7":
                print("Thank you for using the Inventory Management System!")
                break
            
            else:
                print("Invalid option. Please try again.")
        
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()