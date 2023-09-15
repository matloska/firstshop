import sqlalchemy as db

Product = db.Table('Product', db.MetaData(),
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('Name', db.String(255), nullable=False),
              db.Column('Description', db.String(255), default="A new item in our store"),
              db.Column('Price', db.Float(), nullable=False)
              )