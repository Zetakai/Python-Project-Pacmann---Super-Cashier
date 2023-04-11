import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import tabulate
import uuid


class Transaction:

    # class attribute
    __transaction_id = None
    __cart = []

    # initialize customer id
    def __init__(self):
        self.__transaction_id = str(uuid.uuid4())

    def __check_discount(self, amount, price):
        if (amount*price > 500000):
            discount = '7%'
            total_price_after_discount = amount*price*0.93
        elif (amount*price > 300000):
            discount = '6%'
            total_price_after_discount = amount*price*0.94
        elif (amount*price > 200000):
            discount = '5%'
            total_price_after_discount = amount*price*0.95
        else:
            discount = '0%'
            total_price_after_discount = amount*price
        return [discount, total_price_after_discount]

    # call this function to add item into cart
    def add_item(self, items):
        try:
            if not any(item['name'].lower() == items[0].lower() for item in self.__cart):
                discount_n_total = self.__check_discount(items[1], items[2])
                self.__cart.append(
                    {'name': items[0], 'transaction_id': self.__transaction_id,
                     'amount': items[1], 'price': items[2],'total_price': items[1]*items[2],
                     'discount': discount_n_total[0],
                     'total_price_after_discount': discount_n_total[1]})
            else:
                raise Exception('Add new item instead or update your item')
        except Exception as e:
            print(e)

    # call this function to update item name
    def update_item_name(self, name, updated_name):
        try:
            update = next(
                item for item in self.__cart if item['name'].lower() == name.lower())
            update['name'] = updated_name
        except:
            print("Item name is not found")

    # call this function to update item amount
    def update_item_qty(self, name, updated_amount):
        try:
            update = next(
                item for item in self.__cart if item['name'].lower() == name.lower())
            update['amount'] = updated_amount
            update['total_price'] = update['amount']*update['price']
            discount_n_total = self.__check_discount(
                updated_amount, update['price'])
            update['discount'] = discount_n_total[0]
            update['total_price_after_discount'] = discount_n_total[1]
        except:
            print("Item name is not found")

    # call this function to update item price
    def update_item_price(self, name, updated_price):
        try:
            update = next(
                item for item in self.__cart if item['name'].lower() == name.lower())
            update['price'] = updated_price
            update['total_price'] = update['amount']*update['price']
            discount_n_total = self.__check_discount(
                update['amount'], updated_price)
            update['discount'] = discount_n_total[0]
            update['total_price_after_discount'] = discount_n_total[1]
        except:
            print("Item name is not found")

    # call this function to delete item
    def delete_item(self, name):
        try:
            if not any(item['name'].lower() == name.lower() for item in self.__cart):
                raise NameError("Item name is not found")
            else:
                res = list(
                    filter(lambda i: i['name'].lower() != name.lower(), self.__cart))
                self.__cart = res
        except NameError as e:
            print(e)

    # call this function to reset cart
    def reset_transaction(self):
        self.__cart.clear()
        print("Transaction is reset")

    # call this function to check order in cart
    def check_order(self):
        try:
            dataset = self.__cart
            header = dataset[0].keys()
            rows = [x.values() for x in dataset]
            print(tabulate.tabulate(rows, header))
        except:
            print("Your order list is empty")

    # call this function to checkout all item in cart
    def check_out(self):
        try:
            total_price = 0
            total_price_after_discount = 0
            for item in self.__cart:
                total_price += item["total_price"]
                total_price_after_discount += item["total_price_after_discount"]
            if self.__cart:
                self.insert_to_table()
            else:
                raise ValueError("Your order list is empty")
        except ValueError as e:
            print(e)
        finally:
            self.check_order()
            print(f'Succesfully checked out')
            print(f'total : {total_price}')
            print(f'total after discount : {total_price_after_discount}')
            self.reset_transaction()

    # call this function to insert transaction into SQLite table
    def insert_to_table(self):
        engine = db.create_engine('sqlite:///supercashier.db', echo=True)
        # conn = engine.connect()
        metadata = db.MetaData()
        transactions_table = db.Table('transactions', metadata,
                                      db.Column(
                                          'id', db.Integer, primary_key=True, autoincrement=True),
                                      db.Column(
                                          'transaction_id', db.String),
                                      db.Column('name', db.String),
                                      db.Column('amount', db.Integer),
                                      db.Column('price', db.Integer),
                                      db.Column('total_price', db.Integer),
                                      db.Column('discount', db.String),
                                      db.Column(
                                          'total_price_after_discount', db.Float),
                                      )
        metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        for item in self.__cart:
            row = transactions_table.insert().values(**item)
            session.execute(row)
        session.commit()
        session.close()
