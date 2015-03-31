# coding=utf8



from runserver import db



class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)




if __name__ == "__main__":
    print Shop.metadata.create_all(db.engine)
    shop = Shop(name='name1')
