import mysql.connector as c
mydb= c.connect(host="localhost", user="root",password="cvr@123",database="05db")
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE employee (eid INT, ename VARCHAR(20),edept varchar(10))")
# ename=input("Enter your name")
# eid = input("Enter your id")
# edept=input(("Enter your dept"))
# mycursor.execute("insert into employee values(%s,%s,%s)",(eid, ename,edept))
mycursor.execute("UPDATE employee SET ename = 'Swathi' WHERE eid = 50")
mycursor.execute("DELETE FROM employee WHERE eid = 41")
mycursor.execute("select * from employee order by ename")
emp=mycursor.fetchall();
print(emp)
mycursor.execute("select * from employee")
emp=mycursor.fetchall();
for employee in emp:
    print(employee)
mydb.commit()
mycursor.execute("select * from employee where eid between 70 and 90")
emp=mycursor.fetchall();
print(emp)
mycursor.execute("SELECT * FROM employee WHERE ename='Rani'")
emp = mycursor.fetchall()
print(emp)
