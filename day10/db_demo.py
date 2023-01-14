import mysql.connector

con = mysql.connector.connect(
    host="localhost",#DB HOST
    user="root", #DBUsername
    password="admin",#DB Password
    # database='Subhendu_db'
)
print(con)

cur = con.cursor()
cur.excute("CREATE TABLE EMP")