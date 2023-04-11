# Python-Project-Pacmann - Super-Cashier
### Muhammad Farid Zaki / muhammadfarid.zaki@gmail.com

# PROJECT BACKGROUNDS
Super Cashier is a quick shopping support tool, helping to automatically list their item into cart and print the invoice to the customers then record the transaction into database

# FEATURE REQUIREMENTS
1. Customers must be able to add or update items
2. Customers must be able to edit items on the list
3. Customers must be able to erase 1 items on the list
4. Customers must be able to reset their transaction
5. Customers must be able to see total transaction before proceed to pay
6. Customers can checkout their items
7. Customers get the "error message" when there's error on the input
8. Transaction then exported to sqlite

<!---# FLOWCHART
![Flowchart](https://github.com/nuralamsaputra/Cashier-Project/blob/master/img/flowchart%20super%20cashier.drawio.png)--->

# MODULES EXPLANATION

### 1. Libraries
![libraries](img/functions/libraries.png)

Create class transaction with atribute self.cart to put the items in list
### 2. Class Transaction
![Transaction](https://github.com/nuralamsaputra/Cashier-Project/blob/master/img/02.%20class%20Transaction.png)

Add item with parameters item name, item quantity and item price in dictionary per item and append the next item into the list
### 3. Add Item
![Add Item](img/functions/add_item.png)

Change certain item name in the list, with found list as the filtered item 
### 4. Update Item Name
![Update Item Name](img/functions/update_name.png)

Change certain item quantity in the list, with found list as the filtered item
### 5. Update Item Quantity
![Update Item Quantity](img/functions/update_amount.png)

Change certain item price in the list, with found list as the filtered item
### 6. Update Item Price
![Update Item Price](img/functions/update_price.png)

Delete certain item in the list, with found list as the filterd item
### 7. Delete Item
![Delete Item](img/functions/delete_item.png)

Reset the transaction list and start anew
### 9. Reset Transaction
![Reset Transaction](img/functions/reset_transaction.png)

Check the transaction list in form of table using pretty table library, consist of item name, item quantity, item price and price total of item
### 10. Check Order
![Check Order](img/functions/check_order.png)

Check out items from cart and export the data to database
### 11. Check out
![Check Order](img/functions/check_out.png)

Insert to table function
### 11. Insert to table
![Insert to table](img/functions/insert_to_table.png)


Show how much amount customer need to pay, if certain amount is achieved customers will get discount.
# HOW TO USE 

### 1. Download or Clone this project
### 2. Make sure to you have installed python and libraries globally
### 3. run App.py
### 4. Ready to use

# TEST CASE

### Following images is example of how i use the module using jupyter notebook

![Test Case](img/test_cases/run_script.png)

![Test Case](img/test_cases/run_1.png)

![Test Case](img/test_cases/run_2.png)

![Test Case](img/test_cases/run_3.png)

![Test Case](img/test_cases/run_4.png)

![Test Case](img/test_cases/run_5.png)

![Test Case](img/test_cases/run_6.png)

![Test Case](img/test_cases/run_7.png)

![Test Case](img/test_cases/run_8.png)

![Test Case](img/test_cases/run_9.png)

# CONCLUSION

I believe this python program will worked as intended and with comments and suggestion it will improve far better.
