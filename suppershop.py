#-----------------------------
# SupperShop  Management System
# ------------------------------

# ------------------------------
# Read Users from Product.info File
# ------------------------------
def load_products(filename="Products.info.txt"):
    with open(filename, "r") as file:
        products = [line.strip().split(",") for line in file]
    return products

# ------------------------------
# Read sales from Product.update File
# ------------------------------
def load_sales(filename="Products.update.txt"):
    with open(filename, "r") as file:
        sales_products = [line.strip().split(",") for line in file]
    return sales_products



# ------------------------------
# Get products by unique ID
# ------------------------------
def get_products_by_id(products):
    while True:
        try:
            product_id = int(input("Enter UNIQUE ID of the product : "))
            #if 1 <= product_id <= 10:
            for product in products:
                if int(product[0]) == product_id:
                    product_name= product[1]
                    product_price = float(product[2])
                    print(f"\nTHE PRODUCT NAME IS, {product_name}!\n")
                    return product_id, product_name,product_price
            print("Product ID not found.\n")
            #else:
               # print("Invalid Product ID. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# ------------------------------
# Product Entry Function (Modified with inventory update)
# ------------------------------
def product_entry(product_id, product_name, product_price, products):
    from datetime import datetime
    today = datetime.now().strftime("%d-%m-%Y")

    while True:
        try:
            product_count = int(input("Quantity: "))
            break
        except ValueError:
            print("Please enter a valid number for quantity.")

    updated_products = []
    remaining_stock = None

    for product in products:
        if int(product[0]) == product_id:
            current_stock = int(product[4])
            if product_count > current_stock:
                print(f"❌ Not enough stock! Available: {current_stock}")
                return
            remaining_stock = current_stock - product_count
            product[4] = str(remaining_stock)   # ✅ only stock reducing in info file
        updated_products.append(product)

    # Rewrite Products.info.txt in clean aligned format
    with open("Products.info.txt", "w") as file:
        for product in updated_products:
            line = "{:<2}, {:<12}, {:<4}, {:<4}, {:<5}\n".format(
                product[0].strip(),
                product[1].strip(),
                product[2].strip(),
                product[3].strip(),
                product[4].strip()
            )
            file.write(line)

    # Save sale record in Products.update.txt (with remaining stock)
    price = product_count * product_price
    with open("Products.update.txt", "a") as product_file:
        product_file.write(f"{today:<12}, {product_id:<5}, {product_count:<5}, {price:<8}, {remaining_stock}\n")

    print(f"\n✅ Sale saved! Remaining stock of {product_name}: {remaining_stock}\n")




# ------------------------------
# To find Total sale
# ------------------------------
def total_sales():
    summ=0
    filename = "Products.update.txt"

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            summ = summ + float(parts[3])
        print(summ)
    return parts

# ------------------------------
# To find any days total sales
# ------------------------------

def daily_sales():
    print("total sales function called")

    # Ask for full date input from user
    input_date = input("Enter date (e.g., 7-5-2025): ")  # day-month-year
    try:
        day, month, year = map(float, input_date.strip().split("-"))
    except ValueError:
        print("Invalid date format! Please enter as DD-MM-YYYY\n")
        return

    total_daily_sale =0

    try:
        with open("Products.update.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                # Extract date from line (assumed to be in parts[0])
                date_parts = parts[0].split("-")
                if len(date_parts) != 3:
                    continue  # Skip lines that don't have proper date

                file_day = float(date_parts[0])
                file_month = float(date_parts[1])
                file_year = float(date_parts[2])


                if len(parts) >= 4:
                    product_price = float(parts[3])

                    # Check if the user ID and full date match
                    if (day == file_day and
                            month == file_month and
                            year == file_year):
                        total_daily_sale = total_daily_sale + product_price

        print(f"Total sale on {day}-{month}-{year}: {total_daily_sale}\n")

    except FileNotFoundError:
        print("Error: Product.update.txt file not found.\n")
    except Exception as e:
        print(f"An error occurred while counting total meals: {e}\n")

# ------------------------------
# To find product_satus
# ------------------------------
def product_satus(products, sales_products):
    while True:
        try:
            unique_id = int(input("Enter UNIQUE ID of the product : "))
            if 1 <= unique_id <= 10:
                for product in products:
                    if int(product[0]) == unique_id:
                        sale_amount = 0
                        total_sales_amount = 0

                        product_name = product[1].strip()
                        product_price = float(product[2])

                        for sales_product in sales_products:
                            if len(sales_product) >= 4:
                                try:
                                    sales_id = int(sales_product[1].strip())
                                    if unique_id == sales_id:
                                        sold_quantity = float(sales_product[2].strip())
                                        total_sale = float(sales_product[3].strip())
                                        sale_amount += sold_quantity
                                        total_sales_amount += total_sale
                                except ValueError:
                                    continue  # skip faulty lines

                        print(f"\nID    :   {unique_id}")
                        print(f"NAME  :   {product_name}")
                        print(f"PRICE :   {product_price}")
                        print(f"SOLD  :   {sale_amount}")
                        print(f"SALE  :   {total_sales_amount}")
                        return unique_id, product_name, product_price
                print("Product ID not found.\n")
            else:
                print("Invalid Product ID. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")





# ------------------------------
# Main Menu
# ------------------------------
def main():
    while True:
        print("\nPress 1 for Entry")
        print("Press 2 for Total sale")
        print("Press 3 to know a random day's sale")
        print("Press 4 for product status")
        print("Press 0 to Exit\n")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                products = load_products()
                product_id, product_name, product_price = get_products_by_id(products)
                product_entry(product_id, product_name, product_price,products)
            elif choice == 2:
                total_sales()
            elif choice == 3:
                daily_sales()
            elif choice == 4:
                products = load_products()
                sales_products = load_sales()
                product_satus(products, sales_products)
            elif choice == 0:
                print("Exiting the program. Goodbye!")
                break  # Exit the loop and program
            else:
                print("Invalid input. Please press 1, 2, 3, 4, or 5.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# ------------------------------
# Program Entry Point
# ------------------------------
if __name__ == "__main__":
    main()