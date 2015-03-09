# coding=utf8

from peewee import MySQLDatabase

db = MySQLDatabase("doer", user="root", passwd="root", charset = "utf8")

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db
