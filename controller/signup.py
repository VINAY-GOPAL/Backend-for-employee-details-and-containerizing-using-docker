from app import app
from model.employee import employee
obj = employee()

@app.route("/getallemp")
def emp_getall():
    return obj.emp_getall_model()

@app.route("/getalldept")
def dept_getall():
    return obj.dept_getall_model()

@app.route("/empcountbydept")
def emp_count_dept():
    return obj.emp_countby_dept()
    
@app.route("/empname/<ename>")
def emp_name(ename):
    return obj.emp_name_model(ename)