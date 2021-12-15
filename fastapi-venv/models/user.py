from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Integer, String 
users = Table(
    'users', meta,
    Column('id', Integer,primary_key=true),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)