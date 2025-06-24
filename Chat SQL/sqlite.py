import sqlite3

#connect to sqlite3
connection=sqlite3.connect("student.db")

#create a cursor object to insert record, create table
cursor=connection.cursor()

#create a table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

#insert into the table
cursor.execute('''Insert into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute("INSERT INTO STUDENT VALUES('Anita', 'Machine Learning', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi', 'Data Engineering', 'A', 92)")
cursor.execute("INSERT INTO STUDENT VALUES('Sneha', 'Cyber Security', 'C', 78)")
cursor.execute("INSERT INTO STUDENT VALUES('Arjun', 'AI Ethics', 'B', 88)")
cursor.execute("INSERT INTO STUDENT VALUES('Meena', 'Cloud Computing', 'A', 95)")
cursor.execute("INSERT INTO STUDENT VALUES('Vikram', 'DevOps', 'B', 81)")
cursor.execute("INSERT INTO STUDENT VALUES('Sara', 'Computer Vision', 'A', 89)")
cursor.execute("INSERT INTO STUDENT VALUES('Karan', 'NLP', 'C', 74)")
cursor.execute("INSERT INTO STUDENT VALUES('Priya', 'Big Data', 'B', 82)")
cursor.execute("INSERT INTO STUDENT VALUES('Rohit', 'Quantum Computing', 'A', 91)")

#Display all the records
print("The inserted records are")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

#commit the changes in the database
connection.commit()
connection.close()