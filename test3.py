import mysql.connector as conn
mydb = conn.connect(host = "localhost", user = "root", passwd = "KuShi025@")
cursor = mydb.cursor()
cursor.execute("select Employee_Id, Empl_email_id from shivam.ineuron")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[-1]))


58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no"
