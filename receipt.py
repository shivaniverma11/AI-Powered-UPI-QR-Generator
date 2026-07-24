import datetime

def generate_receipt(name, upi):
    file_name = "receipt.txt"

    with open(file_name, "w") as f:
        f.write("------ PAYMENT RECEIPT ------\n")
        f.write(f"Name: {name}\n")
        f.write(f"UPI ID: {upi}\n")
        f.write(f"Date: {datetime.datetime.now()}\n")

    return file_name