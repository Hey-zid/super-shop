# 🛒 SupperShop Management System  

A simple **Python-based shop management system** to manage product inventory, record sales, track daily and total revenue, and monitor product status.  

This project is designed for **small businesses and students** who want to practice file handling, structured data management, and basic reporting in Python.  

---

## 🚀 Features  

✔️ **Product Entry & Sale Recording**  
- Select products by unique ID.  
- Enter sales quantity.  
- Automatically updates inventory in `Products.info.txt`.  
- Logs each transaction in `Products.update.txt` (with date, quantity, total price, and remaining stock).  

✔️ **Total Sales Report**  
- Shows total sales from all recorded transactions.  

✔️ **Daily Sales Report**  
- Enter a specific date (DD-MM-YYYY).  
- System calculates total sales for that day.  

✔️ **Product Status Check**  
- Enter product ID.  
- Shows product details, sold quantity, and total revenue generated.  

✔️ **Show All Inventory**  
- Displays a clean table of current stock, selling price, buying cost, and product IDs.  

✔️ **File-Based Storage**  
- Products and sales data are stored in plain text files:  
  - `Products.info.txt` → product details & stock.  
  - `Products.update.txt` → all sales history.  

---

## 📂 File Structure  

```
📦 SupperShop-Management-System
 ┣ 📜 main.py               # Main program
 ┣ 📜 Products.info.txt     # Product details (ID, name, price, cost, stock)
 ┣ 📜 Products.update.txt   # Sales transactions
 ┗ 📜 README.md             # Documentation
```

---

## 📝 Product Data Format (`Products.info.txt`)  

```
ID , Name         , Selling Price , Buying Price , Stock
1  , Rice         , 80            , 70           , 260
2  , Sugar        , 120           , 100          , 500
3  , Salt         , 40            , 35           , 500
...
```

---

## 📝 Sales Data Format (`Products.update.txt`)  

```
Date        , Product ID , Quantity , Total Price , Remaining Stock
11-07-2025  , 1          , 2        , 160.0       , 258
11-07-2025  , 10         , 4        , 300.0       , 446
11-07-2025  , 4          , 8        , 640.0       , 392
...
```

---

## ⚡ How to Use  

1. Clone or download this project.  
2. Make sure you have **Python 3** installed.  
3. Prepare your `Products.info.txt` file with initial inventory.  
4. Run the program:  

```bash
python main.py
```

5. Choose from the menu options:  
   - `1` → Product Entry / Sale Entry  
   - `2` → View Total Sales  
   - `3` → View Sales of a Specific Day  
   - `4` → Product Status Report  
   - `5` → Show Inventory  
   - `0` → Exit  

---

## 📊 Example Output  

### Inventory View
```
ID    Name            Price      Cost       Stock
-------------------------------------------------------
1     Rice            80         70         260
2     Sugar           120        100        500
3     Salt            40         35         500
...
```

### Product Status
```
ID    : 2
NAME  : Sugar
PRICE : 120.0
SOLD  : 30
SALE  : 3600.0
```

---

## 🎯 Future Improvements  

- Add **GUI interface** for easier usage.  
- Export reports to **Excel/CSV/PDF**.  
- Add **user login system** for shop staff.  
- Include **profit/loss calculation**.  

---

## 🧑‍💻 Author  

👤 **Bayazid Hossain Parvez**  
- 💼 CSE Undergraduate | Southeast University, Dhaka  
- 🌍 Passionate about **business & technology**  
- 🔗 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com/Hey-zid)  

---

✨ If you find this useful, don’t forget to ⭐ star the repo and share it!  
