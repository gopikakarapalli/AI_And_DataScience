import mysql.connector

mydb = mysql.connector.connect(
      host="209.99.16.245",
      user="beovopkf_beo",
      passwd="Beo@@123"
      )

#print(mydb)

mycursor=mydb.cursor()
#mycursor.execute("CRATE DATABASE databaseName")
mycursor.execute("SHOW DATABASES")


for db in mycursor:
      print(db)
mycursor.close()

print('--------------------------------------------------------')

mydb = mysql.connector.connect(
      host="209.99.16.245",
      user="beovopkf_beo",
      passwd="Beo@@123",
      database ="beovopkf_demo"
      )
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE students_1(name VARCHAR(250),age INTEGER(10))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
      print(tb)

print("------------------------------------------------------------" )
'''
mycursor.execute("""INSERT INTO students(name,age) VALUES(%s,%s)""",("Gopi",26))
studentlist = [("A",20),
               ("b",20),
               ("c",20),
               ("d",20),
               ("e",20),
               ("f",20),]
mycursor.executemany("INSERT INTO students(name,age)VALUES(%s,%s)",studentlist)
mydb.commit()
'''
# to read table:

mycursor.execute("SELECT * FROM students") # * all col in students

mydata = mycursor.fetchall()
for row in mydata:
      print(row)

mycursor=mydb.cursor()
sql = "SELECT * FROM students WHERE age = 26"
#sql = "SELECT * FROM students WHERE name LIKE 'A%'"
#sql = "SELECT * FROM students WHERE name LIKE '%o%'"

mycursor.execute(sql)

mydata = mycursor.fetchall()
for row in mydata:
      print(row)
print('-----------------update---------------------------')
#update data

mycursor = mydb.cursor()

#mycursor.execute("UPDATE students SET age = 13 WHERE name = 'A'")
#mydb.commit()
#mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
#mycursor.execute("SELECT * FROM students ORDER BY name")
mycursor.execute("SELECT * FROM students ORDER BY name DESC")
mydata = mycursor.fetchall()
for row in mydata:
      print(mydata)

print('---------------------DELETE & DROP--------------------------')

#mycursor.execute("DELETE FROM students WHERE name ='f'")

#mycursor.execute("DROP TABLE students_1")
mycursor.execute("DROP TABLE IF EXISTS students_1")


















