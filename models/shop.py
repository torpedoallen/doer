# coding=utf8



from lib.database import BaseModel
from peewee import CharField, DateTimeField, ForeignKeyField



class Shop(BaseModel):
    name = CharField()

class ItemList(BaseModel):
    name = CharField()

class ShopKeeper(BaseModel):
    name = CharField()

class Item(BaseModel):
    name = CharField()
    created_at = DateTimeField()
    shop = ForeignKeyField(Shop)
    item_list = ForeignKeyField(ItemList)
    shop_keeper = ForeignKeyField(ShopKeeper)
