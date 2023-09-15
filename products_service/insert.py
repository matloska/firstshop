import sqlalchemy as db
from tables.product import Product

engine = db.create_engine('sqlite:///products.sqlite')

Product.metadata.create_all(engine) 

conn = engine.connect()


q = db.insert(Product).values(Id=1, Name='Onion',Description='Some kind of onion', Price=33.45)
res = conn.execute(q)
conn.commit()

q = db.insert(Product).values(Id=2, Name='Garlic',Description='Great garlic', Price=22.33)
res = conn.execute(q)
conn.commit()

all_products = conn.execute(Product.select()).fetchall()
print(all_products)

conn.close()