from typing import Any
import sqlite3


class Table:
    def __init__(self,db_name,table_name,columns_definition=None):
        self.db_name= db_name
        self.table_name = table_name

        if columns_definition:
            self.create_table(columns_definition)

    def create_table(self, columns_definition):
        query = f'CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_definition})'
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(query)


    def insert(self,**kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?' for _ in kwargs])
        query  = f'INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})'
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(query,tuple(kwargs.values()))

    def select(self,**cond):
        query = f"SELECT * FROM {self.table_name}"
        if cond:
            where = "AND ".join([f"{k} = ?" for k in cond.keys()])
            query += f" WHERE {where}"
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.execute(query,tuple(cond.values()))
                return cursor.fetchall()
        else:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.execute(query)
                return cursor.fetchall()


users = Table('test.db','users','id INTEGER PRIMARY KEY, name TEXT')
users.insert(id=1,name = "Алиса")
users.insert(id=2,name = 'Боб')
print(users.select())
print(users.select(name="Алиса"))