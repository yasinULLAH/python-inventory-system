# Python Inventory Management System

A simple yet powerful inventory management system built with Python, using CSV files for data storage. Perfect for small businesses and shops to manage their product inventory, track stock levels, and monitor transactions.

## 🚀 Features

- **Product Management**
  - Add new products with details (name, quantity, price, category)
  - Set reorder levels for automatic low stock alerts
  - Generate unique product IDs for easy tracking

- **Inventory Control**
  - Record stock additions and removals
  - Track transaction history
  - Monitor low stock items
  - Generate inventory reports

- **Data Management**
  - CSV-based data storage
  - Transaction logging with timestamps
  - Data persistence across sessions

## 📋 Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yasinULLAH/python-inventory-system.git
```

2. Navigate to the project directory:
```bash
cd python-inventory-system
```

3. Run the application:
```bash
python inventory_system.py
```

## 💻 Usage

The system provides an interactive menu with the following options:

1. **Add New Product**
   - Enter product details (name, quantity, price, category)
   - System generates a unique product ID

2. **Record Stock In**
   - Add inventory to existing products
   - Record transaction details and notes

3. **Record Stock Out**
   - Remove inventory from stock
   - Track outgoing transactions

4. **View Inventory Report**
   - Display current stock levels
   - Show product details and categories

5. **View Low Stock Alert**
   - Check items below reorder level
   - Prevent stockouts

6. **View Transaction History**
   - Track all inventory movements
   - Filter transactions by product ID

## 📁 File Structure

```
python-inventory-system/
├── inventory_system.py
├── data/
│   ├── inventory.csv
│   └── transactions.csv
└── README.md
```

## 📊 Data Storage

The system uses two CSV files for data storage:

### inventory.csv
Stores product information:
- Product ID
- Name
- Quantity
- Price
- Category
- Reorder Level

### transactions.csv
Records all inventory movements:
- Transaction ID
- Product ID
- Transaction Type (IN/OUT)
- Quantity
- Date
- Notes

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Yasin ULLAH**
- GitHub: [@yasinULLAH](https://github.com/yasinULLAH)

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this system
- Inspired by the needs of small businesses for simple inventory management

## 📞 Support

If you encounter any issues or have questions, please create an issue in the GitHub repository.

---
⭐️ If you find this project helpful, please give it a star on GitHub! ⭐️
