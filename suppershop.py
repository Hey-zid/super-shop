#-----------------------------
# SupperShop  Management System
# ------------------------------

# ------------------------------
# Read Users from File
# ------------------------------
def load_products(filename="Products.info.txt"):
    with open(filename, "r") as file:
        products = [line.strip().split(",") for line in file]
    return products



# ------------------------------
# Get products by unique ID
# ------------------------------
def get_products_by_id(products):
    while True:
        try:
            product_id = int(input("Enter UNIQUE ID of the product : "))
            if 1 <= product_id <= 10:
                for product in products:
                    if int(product[0]) == product_id:
                        product_name= product[1]
                        product_price = float(product[2])
                        print(f"\nTHE PRODUCT NAME IS, {product_name}!\n")
                        return product_id, product_name,product_price
                print("Product ID not found.\n")
            else:
                print("Invalid Product ID. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# ------------------------------
# Product Entry Function
# ------------------------------
def product_entry(product_id, product_name,product_price):
    print("Product entry function is called.\n")
    from datetime import datetime
    today = datetime.now().strftime("%d-%m-%Y")
    while True:
        try:
            product_count = int(input("Quantity: "))

            break
        except ValueError:
            print("Please enter a valid number for meals.")
    price = (product_count * product_price)
    with open("Products.update.txt", "a") as product_file:
        product_file.write(f"{today:<12}, {product_id:<8}, {product_count:<5},{price}\n")

    print("\nYour product entry saved successfully!\n")


# ------------------------------
# To find Total sale
# ------------------------------
def total_sales():
    sum=0
    filename = "Products.update.txt"

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            sum = sum + float(parts[3])
        print(sum)
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
def product_satus():
    print('Work in process........')




# ------------------------------
# Main Menu
# ------------------------------
def main():
    print("Press 1 for Entry",'\n'"Press 2 for Total sale",'\n'"Press 3 to know a random days sale",'\n'"Press 4 for product status")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                products = load_products()
                product_id, product_name,product_price = get_products_by_id(products)
                product_entry(product_id, product_name,product_price)
                break
            elif choice == 2:
                total_sales()
                break
            elif choice == 3:
                daily_sales()
                break
            elif choice == 4:
                product_satus()
                break
            else:
                print("Invalid input. You must press 1 or 2.\n")
        except ValueError:
            print("Please enter a valid number.\n")


# ------------------------------
# Program Entry Point
# ------------------------------
if __name__ == "__main__":
    main()