from flask import Flask
import sqlalchemy as db
from tables.product import Product
import json

app = Flask(__name__)

engine = db.create_engine('sqlite:///products.sqlite')

@app.get("/api/products")
def products():

    conn = engine.connect()

    rows = conn.execute(Product.select()).fetchall()

    conn.close()

    all_products=[]
    for row in rows:
        lr = list(row)
        res = {}
        for i in range(len(lr)):
            res[Product.columns[i].name]=lr[i]

        all_products.append(res)

    print(all_products)
    print(type(all_products))
    print(json.dumps(all_products))

    return json.dumps(all_products)

if __name__=="__main__":
    app.run(debug=True)