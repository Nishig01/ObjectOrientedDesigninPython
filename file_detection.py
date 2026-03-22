# Python file detection
import os

file_path = "test"
ecommerce_file_path = "ecommerce"
if os.path.exists(ecommerce_file_path):
    print(f"The file '{ecommerce_file_path}' exists")
    if os.path.isfile(ecommerce_file_path):
        print(f"The file '{ecommerce_file_path}' is a file")
    elif os.path.isdir(ecommerce_file_path):
        print(f"The file '{ecommerce_file_path}' is a directory")

else:
    print(f"The file '{ecommerce_file_path}' does not exist")


