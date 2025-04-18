import hashlib

def get_file_hash(file_name):
    try:
        with open(file_name, "rb") as my_file:
            file_data = my_file.read()
            hash_object = hashlib.sha256(file_data)
            file_hash = hash_object.hexdigest()
            return file_hash
    except FileNotFoundError:
        print("File not found!")
        return None

file_to_check = "example.txt"

try:
    with open("originalhash.txt", "r") as f:
        original_hash = f.read().strip()
except FileNotFoundError:
    print("originalhash.txt not found!")
    original_hash = ""

new_hash = get_file_hash(file_to_check)

if new_hash:
    print("File Hash:", new_hash)
    if new_hash == original_hash:
        print("File is the same (no changes).")
    else:
        print("File has been changed!")