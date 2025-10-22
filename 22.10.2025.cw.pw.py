#підключення до бази данних postgres   через sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from sqlalchemy import  create_engine, MetaData

with open('credentials.json') as file:
    data = json.load(file)
    login = data['login']
    password  = data['password']

DATABASE_URL = f'postgresql+pg8000://{login}:{password}@localhost/hospital'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()




#отриманння данних з таблиці

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables #отримання всіх таблиць з бази данних

for table_name in tables:
    print(f"Table: {table_name}")
    table = tables[table_name]
    for column in table.c:
        print(f"  Column: {column.name}, Type: {column.type}")

#виконання запиту
from sqlalchemy import text

query_text = """
SELECT *
FROM DOCTORS
WHERE SALARY > 90000
"""
# Виконання запиту
#переведення запиту в  правильний формат
query_text = text(query_text)


query = session.execute(query_text)

#виведення результатів запиту
# вказати які результати потрібно вивести
#наприклад всі результати
# 1 ryadok
results = query.fetchall()

doctors = tables['doctors']
column_names = doctors.columns.keys()
print(column_names)


for row in results:
    print(row)
    print(row.salary)  # Припустимо, що є стовпець 'salary')