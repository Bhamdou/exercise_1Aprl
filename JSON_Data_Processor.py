import json

def read_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_product(data, product_name):
    for product in data:
        if product['name'] == product_name:
            return product
    return None

def increase_product_price(product, percentage):
    product['price'] *= (1 + percentage / 100)

def update_product_quantity(product, new_quantity):
    product['quantity'] = new_quantity

def add_product(data, product_name, price, quantity):
    new_product = {"name": product_name, "price": price, "quantity": quantity}
    data.append(new_product)

def remove_product(data, product_name):
    product = find_product(data, product_name)
    if product is not None:
        data.remove(product)

def main():
    file_path = 'products.json'
    products_data = read_json_data(file_path)

    print("\nJSON Data Processor")
    print("1. Increase Product Price")
    print("2. Update Product Quantity")
    print("3. Add Product")
    print("4. Remove Product")
    print("5. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            product_name = input("Enter product name: ")
            percentage = float(input("Enter percentage increase: "))
            product = find_product(products_data, product_name)
            if product:
                increase_product_price(product, percentage)
            else:
                print("Product not found.")
        elif choice == 2:
            product_name = input("Enter product name: ")
            new_quantity = int(input("Enter new quantity: "))
            product = find_product(products_data, product_name)
            if product:
                update_product_quantity(product, new_quantity)
            else:
                print("Product not found.")
        elif choice == 3:
            product_name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add_product(products_data, product_name, price, quantity)
        elif choice == 4:
            product_name = input("Enter product name: ")
            remove_product(products_data, product_name)
        elif choice == 5:
            write_json_data(products_data, file_path)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


