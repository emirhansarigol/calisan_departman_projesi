from crud import EmployeeManager
db=EmployeeManager()
# db.create_employee('Servet Demir', '2020-01-15', 30000)

emp1=db.get_employee(1)

db.update_salary(1,3500000)

# db.delete_employee(9)

db.get_all_employees()
