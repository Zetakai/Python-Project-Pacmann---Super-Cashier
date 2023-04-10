from Cashier import Transaction
from ReadDB import read_db

def inputInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Please enter number only')
            continue


def leave():
    # Letting user know that selected task has been executed
    print("""
    Thank you for using Super Cashier System. See you next time ~
    ------------------------------------------------------
    "Customer satisfaction is out top priority"
    """)
    exit()


def start_program():
    
    print("........... Welcome to Super Cashier System...........")
    transaction = Transaction()

    def main_menu():
        # User interface layout
        print(""" 
        1. Add New Item
        2. Update Item Name
        3. Update Item Amount
        4. Update Item Price
        5. Delete Item
        6. Reset Transaction
        7. Check Order
        8. Check Out
        9. Check Transactions Database
        10. Exit
        """)

        # Prompting user to enter any task above
        choice = input("Enter task no: ")
        print(".......................................")

        # After user enter task no, respective task functions will be executed
        if(choice == '1'):
            name = input("Item name:")
            amount = inputInt("Item amount:")
            price = inputInt("Item price:")
            transaction.add_item([name, amount, price])
            transaction.check_order()
            main_menu()
        elif(choice == '2'):
            name = input("Item name:")
            updated_name = input("Change item name to:")
            transaction.update_item_name(name, updated_name)
            transaction.check_order()
            main_menu()
        elif(choice == '3'):
            name = input("Item name:")
            amount = inputInt("Change item amount to:")
            transaction.update_item_qty(name, amount)
            transaction.check_order()
            main_menu()
        elif(choice == '4'):
            name = input("Item name:")
            price = inputInt("Change item price to:")
            transaction.update_item_price(name, price)
            transaction.check_order()
            main_menu()
        elif(choice == '5'):
            name = input("Item name:")
            transaction.delete_item(name)
            transaction.check_order()
            main_menu()
        elif(choice == '6'):
            transaction.reset_transaction()
            main_menu()
        elif(choice == '7'):
            transaction.check_order()
            main_menu()
        elif(choice == '8'):
            transaction.check_out()
            start_program()
        elif(choice == '9'):
            read_db()
            main_menu()
        elif(choice == '10'):
            leave()
        # If user key in no outside of available inputs, main menu will be displayed
        else:
            main_menu()
    main_menu()


# Displaying main menu when main.py file is executed on terminal
start_program()
