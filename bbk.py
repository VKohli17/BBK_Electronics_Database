import mysql
import pymysql

con = pymysql.connect(host='localhost',
    port=30306,
    user="root",
    password="dna",
    db='bbke',
    cursorclass=pymysql.cursors.DictCursor)

# tmp = sp.call('clear', shell=True)

if(con.open):
    print("Connected")
else:
    print("Failed to connect")

query = "show tables;"

# output a table with the names of all the tables
# with con:
#     cur = con.cursor()
#     cur.execute(query)
#     rows = cur.fetchall()
#     for row in rows:
#         print(row["Tables_in_bbk"])

cur = con.cursor()
cur.execute("desc services;")
for obj in cur:
    print (obj)

query2= "insert into services\
        values(123, 'idklol', 500);"

# cur2= con.cursor()
# cur2.execute(query2)
# for obj in cur2:
#     print (obj)   

query3= "select * from services;"

cur3= con.cursor()
cur3.execute(query3)
for obj in cur3:
    print (obj)

# con.commit()
# cur2.close() 
