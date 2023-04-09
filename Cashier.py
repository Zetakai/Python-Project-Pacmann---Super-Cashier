
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

import uuid
import tabulate

# base class


class Transaction:

    # class attribute
    # customer_id = None
    name = ""
    amount = 0
    price = 0
    total_price = 0
    cart = []

    # initialize customer id
    # def __init__(self):
    #     self.customer_id = uuid.uuid4()

    # call this function to add item into cart
    def add_item(self, items):
        try:
            if not any(item['name'] == items[0] for item in self.cart):
                self.cart.append({'name': items[0], 'amount': items[1],'price': items[2], 'total_price': items[1]*items[2]})
            else:
                raise Exception('Add new item instead or update your item')
        except Exception as e:
            print(e)

    # call this function to update item name
    def update_item_name(self, name, updated_name):
        try:
            update = next(item for item in self.cart if item['name'] == name)
            update['name'] = updated_name
        except:
            print("Item name is not found")
        
    # call this function to update item amount
    def update_item_qty(self, name, updated_amount):
        try:
            update = next(item for item in self.cart if item['name'] == name)
            update['amount'] = updated_amount
            update['total_price'] = update['amount']*update['price']
        except:
            print("Item name is not found")

    # call this function to update item price
    def update_item_price(self, name, updated_price):
        try:
            update = next(item for item in self.cart if item['name'] == name)
            update['price'] = updated_price
            update['total_price'] = update['amount']*update['price']
        except:
            print("Item name is not found")

    # call this function to delete item
    def delete_item(self, name):
        try:
            if not any(item['name'] == name for item in self.cart):
                raise NameError("Item name is not found")
            else:
                res = list(filter(lambda i: i['name'] != name, self.cart))
                self.cart = res
        except NameError as e:
            print(e)


    # call this function to reset cart
    def reset_transaction(self):
        self.name = ""
        self.amount = 0
        self.price = 0
        self.total_price = 0
        self.cart = []

    # call this function to check order in cart
    def check_order(self):
        try:    
            dataset = self.cart
            header = dataset[0].keys()
            rows = [x.values() for x in dataset]
            print(tabulate.tabulate(rows, header))
        except:
            print("Your order list is empty")

    # call this function to checkout all item in cart
    def check_out(self):
        try:
            total=0
            total_without_discount=0
            for item in self.cart:
                total_without_discount+=item['total_price']
                if (item['total_price']>500000):
                    total+=item['total_price']*0.93
                elif (item['total_price']>300000):
                    total+=item['total_price']*0.94
                elif (item['total_price']>200000):
                    total+=item['total_price']*0.95
                else:
                    total+=item['total_price']
            if self.cart:
                self.insert_to_table()
            else:
                raise ValueError("Your order list is empty")
        except ValueError as e:
            print(e)
        finally:
            print(f'total : {total_without_discount}')
            print(f'total after discount : {total}')


    # call this function to insert transaction into SQLite table
    def insert_to_table(self):
        engine = db.create_engine('sqlite:///supercashier.db',echo=True)
        # conn = engine.connect()
        metadata= db.MetaData()
        transactions_table=db.Table('transactions',metadata,
                                    db.Column('id',db.Integer,primary_key=True,autoincrement=True),
                                    db.Column('name',db.String),
                                    db.Column('amount',db.Integer),
                                    db.Column('price',db.Integer),
                                    db.Column('total_price',db.Integer),
                                    )
        metadata.create_all(engine)
        
        Session = sessionmaker(bind=engine)
        session = Session()
       
        for item in self.cart:
            row = transactions_table.insert().values(**item)
            session.execute(row)

        session.commit()
        session.close()
