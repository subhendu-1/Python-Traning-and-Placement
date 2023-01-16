# import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",#DB HOST
#     user="root", #DBUsername
#     password="admin",#DB Password
#     database="subhendu_db"
# )
# print(con)

# cur = con.cursor()
# # cur.execute("CREATE TABLE emp(eid integer,ename varchar(50));")
# cur.execute("INSERT INTO emp(eid,ename,esel) VALUES(101,"SEUBHENDU",50000)")
# con.commit()



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
#   database="hit_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE hit_db")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")