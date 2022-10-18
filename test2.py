import mysql.connector as conn
mydb = conn.connect(host = "localhost", user = "root", passwd = "KuShi025")
cursor = mydb.cursor()
s = cursor.execute("insert into practice.learn values(10002, 'Shivam Kumar', 'kumarshivam9318@gmail.com', 1000)")

cursor.execute(s)
mydb.commit()
cursor.execute("select * from shivam.ineuron")
for i in cursor.fetchall():
    print(i)