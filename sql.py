import sqlite3

## COnnect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor object to insert record,create table,retrieve
cursor = connection.cursor()
# create table 
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#Insert records

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A','50')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B','100')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C','20')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C','85')''')

## Display all the records
print("The inserted records are ")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
     print(row)

table_profile_info = """CREATE TABLE PROFILE(NAME VARCHAR(25),SEX VARCHAR(25),REGION VARCHAR(25));"""
cursor.execute(table_profile_info)

cursor.execute("INSERT INTO PROFILE VALUES('Darius','M','Pune')")
cursor.execute("INSERT INTO PROFILE VALUES('Bikash','M','Bihar')")
## CLose the connection
connection.commit()
connection.close()
