import csv
import re
import subprocess

choice = input("1.Product Management \n2.Supplier Management \n Enter your choice: \n")
if choice == '1':
    subprocess.call(" Py_project_product.py ", shell=True)
        
elif choice == '2':
    subprocess.call(" Py_project_supplier.py ", shell=True)
else: 
    quit()