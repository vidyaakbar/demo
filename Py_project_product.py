import csv
import re
import subprocess

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# noinspection RegExpUnexpectedAnchor
rule = re.compile(r'/^[0-9]{10,14}$/')

# Define global variables
inventory_fields = ['inventory_id', 'description', 'inventory_stock','price']
inventory_database = 'inventory.csv'

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Inventory Management System")
    print("---------------------------------------")
    print("1. Add New Inventory")
    print("2. View Inventory ")
    print("3. Search Inventory")
    print("4. Update Inventory Details")
    print("5. Delete Inventory Record")
    print("6. Quit")

def add_inventory():
    print("-------------------------")
    print("Add Inventory Information")
    print("-------------------------")
    global inventory_fields
    global inventory_database

    inventory_data = []
    while True:
        try:
            value = int(input("Enter your inventory_id: "))
            inventory_data.append(value)
            break
        except ValueError:
            print("Sorry, Enter valid id.")
            continue

    while True:
        # noinspection PyBroadException
        try:
            description1 = input("Enter description:")
            if description1 != "":
                inventory_data.append(description1)
                break
        except Exception:
            print("please enter description:")
            continue

    while True:
        try:
            inventory_stock = int(input("Enter the stock: "))
            inventory_data.append(inventory_stock)
            break
        except ValueError:
            print("Sorry, Please enter the stock again.")
            continue

    while True:
        try:
            price = int(input("Enter the price: "))
            inventory_data.append(price)
            break
        except ValueError:
            print("Sorry, Please enter the price again.")
            continue

    with open(inventory_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([inventory_data])
        print("inventory added Successfully..")
    input("Press any key to continue")
    return

def view_inventory():
    global inventory_fields
    global inventory_database

    print("--- inventory Records ---")

    with open(inventory_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in inventory_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

def search_inventory():
    global inventory_database
    global inventory_fields

    print("--- Search inventory Record ---")
    id_no = input("Enter ID. to search: ")
    with open(inventory_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_no == row[0]:
                    print("----- Inventory Found -----")
                    print("ID: ", row[0])
                    print("Description: ", row[1])
                    print("Inventory_Stock: ", row[2])
                    print("price: ", row[3])
                    break
        else:
            print("ID. not found in our database")
    input("Press any key to continue")

def update_inventory():
    global inventory_fields
    global inventory_database

    print("--- Update inventory Record ---")
    inventory_id = input("Enter ID. to update: ")
    index_inventory = None
    updated_data = []
    with open(inventory_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if inventory_id == row[0]:
                    index_inventory = counter
                    print("inventory Found: at index ", index_inventory)
                    inventory_data = []
                    for field in inventory_fields:
                        value = input("Enter " + field + ": ")
                        inventory_data.append(value)
                    updated_data.append(inventory_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if the record is found or not
    if index_inventory is not None:
        with open(inventory_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print("Data updated..")
    else:
        print("ID. not found in our database")

    input("Press any key to continue")


def delete_inventory():
    global inventory_fields
    global inventory_database

    print("--- Delete inventory Record ---")
    id_no = input("Enter ID to delete: ")
    inventory_found = False
    updated_data = []
    with open(inventory_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_no != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    inventory_found = True

    if inventory_found is True:
        with open(inventory_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID", id_no, "deleted successfully")
    else:
        print("ID not found in our database")

    print("After deletion the records:")
    with open(inventory_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in inventory_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_inventory()
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        search_inventory()
    elif choice == '4':
        update_inventory()
    elif choice == '5':
        delete_inventory()
    elif choice == '6':
        subprocess.call(" py_user.py ", shell=True)


print("-------------------------------")
print("            Thank you          ")
print("-------------------------------")
