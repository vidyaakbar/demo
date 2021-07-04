import csv
import re
import subprocess
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# noinspection RegExpUnexpectedAnchor
rule = re.compile(r'/^[0-9]{10,14}$/')

# Define global variables
supplier_fields = ['id_no', 'name', 'stock','email','phone', 'location']
supplier_database = 'supplier.csv'

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Inventory Management System")
    print("---------------------------------------")
    print("1. Add New Supplier")
    print("2. View Supplier ")
    print("3. Search Supplier")
    print("4. Update Supplier Details")
    print("5. Delete Supplier Record")
    print("6. Quit")

def add_supplier():
    print("-------------------------")
    print("Add Supplier Information")
    print("-------------------------")
    global Supplier_fields
    global Supplier_database

    supplier_data = []
    while True:
        try:
            value = int(input("Enter your id: "))
            supplier_data.append(value)
            break
        except ValueError:
            print("Sorry, Enter valid id.")
            continue

    while True:
        # noinspection PyBroadException
        try:
            name1 = input("Enter name:")
            if name1 != "":
                supplier_data.append(name1)
                break
        except Exception:
            print("please enter your name:")
            continue

    while True:
        try:
            stock = int(input("enter the stock: "))
            supplier_data.append(stock)
            break
        except ValueError:
            print("Sorry, Please enter the stock again.")
            continue

    while True:
        # noinspection PyBroadException
        try:
            email1 = input("Enter email:")
            if re.search(regex, email1):
                supplier_data.append(email1)
                break
        except Exception:
            continue

    while True:
        try:
            phone1 = int(input("enter your phone: "))
            supplier_data.append(phone1)
            break
        except ValueError:
            print("Sorry, Please enter the phone again.")
            continue

    while True:
        # noinspection PyBroadException
        try:
            location1 = input("Enter location:")
            if location1 != "":
                supplier_data.append(location1)
                break
        except Exception:
            print("please enter your location:")
            continue

    with open(supplier_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([supplier_data])
        print("supplier added Successfully..")
    input("Press any key to continue")
    return


def view_supplier():
    global supplier_fields
    global supplier_database

    print("--- supplier Records ---")

    with open(supplier_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in supplier_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_supplier():
    global supplier_database
    global supplier_fields

    print("--- Search supplier Record ---")
    id_no = input("Enter ID. to search: ")
    with open(supplier_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_no == row[0]:
                    print("----- Supplier Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Stock: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("Location: ", row[5])
                    break
        else:
            print("ID. not found in our database")
    input("Press any key to continue")


def update_supplier():
    global supplier_fields
    global supplier_database

    print("--- Update Supplier Record ---")
    id_no = input("Enter ID. to update: ")
    index_supplier = None
    updated_data = []
    with open(supplier_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_no == row[0]:
                    index_supplier = counter
                    print("supplier Found: at index ", index_supplier)
                    supplier_data = []
                    for field in supplier_fields:
                        value = input("Enter " + field + ": ")
                        supplier_data.append(value)
                    updated_data.append(supplier_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if the record is found or not
    if index_supplier is not None:
        with open(supplier_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print("Data updated..")
    else:
        print("ID. not found in our database")

    input("Press any key to continue")


def delete_supplier():
    global supplier_fields
    global supplier_database

    print("--- Delete Supplier Record ---")
    id_no = input("Enter ID to delete: ")
    supplier_found = False
    updated_data = []
    with open(supplier_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_no != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    supplier_found = True

    if supplier_found is True:
        with open(supplier_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID", id_no, "deleted successfully")
    else:
        print("ID not found in our database")

    print("After deletion the records:")
    with open(supplier_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in supplier_fields:
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
        add_supplier()
    elif choice == '2':
        view_supplier()
    elif choice == '3':
        search_supplier()
    elif choice == '4':
        update_supplier()
    elif choice == '5':
        delete_supplier()
    elif choice == '6':
        subprocess.call(" py_user.py ", shell=True)


print("-------------------------------")
print("            Thank you          ")
print("-------------------------------")
