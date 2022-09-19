import mysql.connector
import json

class employee():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="123456",database="hr")
            self.cur = self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("DB connection error")
    def emp_getall_model(self):
        self.cur.execute("select * from employees")
        result = self.cur.fetchall()
        #print(result)
        if len(result)>0:
            return json.dumps(result, indent=4, default=str)
        else:
            return "No data found"

    def dept_getall_model(self):
        self.cur.execute("select * from departments")
        result = self.cur.fetchall()
        #print(result)
        if len(result)>0:
            return json.dumps(result, indent=4, default=str)
        else:
            return "No data found"

    def emp_countby_dept(self):
        self.cur.execute("select department_name,count(*) as count from employees e join departments d on e.department_id = d.department_id group by department_name ")
        result = self.cur.fetchall()
        #print(result)
        if len(result)>0:
            return json.dumps(result, indent=4, default=str)
        else:
            return "No data found"

    def emp_name_model(self,ename):
        self.cur.execute(f"select * from employees where first_name like '{ename}'")
        result = self.cur.fetchall()
        #print(result)
        if len(result)>0:
            return json.dumps(result, indent=4, default=str)
        else:
            return "No data found"