from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

# create a database engine
engine = create_engine('sqlite:///supercashier.db', echo=True)

# define metadata for table
metadata = MetaData()
transactions_table=Table('transactions',metadata,
                                    Column('id',Integer,primary_key=True),
                                    Column('name',String),
                                    Column('amount',Integer),
                                    Column('price',Integer),
                                    Column('total_price',Integer),
                                    )

# bind table to engine
transactions_table.bind = engine

# select data from table
stmt = select(transactions_table)

# create session
with engine.connect() as conn:
    # execute select statement
    result = conn.execute(stmt)
    # iterate over result set and print each row
    for row in result:
        print(row)
    conn.close()