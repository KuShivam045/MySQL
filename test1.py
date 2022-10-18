from itertools import count
import mysql.connector as conn
mydb = conn.connect(host = "localhost", user = "root", passwd = "KuShi025")
print(mydb)
cursor = mydb.cursor()

# a = "create table Practice.learn(Serial_no int(5) ,Sub_1_name varchar(20), Sub_2_name varchar(20),Sub_3_name varchar(20), Sub_4_name varchar(20))"
# s = cursor.execute("insert into Practice.learn values(10000, 'AI', 'Data Science','Neural Network','Cloud Computing')")
# cursor.execute(s)
# mydb.commit()
q2 = cursor.execute("select * from practice.learn")

# for i in cursor.fetchall(): 
#     print(i)


for j in range(len(cursor.fetchall())):
    print(j)



# cursor.execute("create database shivam")
# cursor.execute("create database Practice")
# cursor.execute("show databases")
# print(cursor.fetchall())
# cursor.execute("create database Practice")

# s = "create table shivam.ineuron(Employee_Id int(10), Emp_name varchar(80), Empl_email_id varchar(30), Emp_salary int(6))"
# s = "create table shivam.ineuron1(Employee_Id int(10), Emp_name varchar(80), Empl_email_id varchar(30), Emp_salary int(6))"
# cursor.execute(s)
# q2 = cursor.execute("select * from practice.learn")
# print(q2)
