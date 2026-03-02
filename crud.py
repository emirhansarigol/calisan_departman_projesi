import os
import django
# bunları yapmazsam bu dosya çalışmaz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_system.settings')
django.setup()


from hr.models import Employee

class EmployeeManager:
    def create_employee(full_name, hire_date, salary, department=None):
        try:
            employee = Employee.objects.create(
                full_name=full_name,
                hire_date=hire_date,
                salary=salary,
                department=department
            )
            print(f"Employee '{employee.full_name}' başarıyla oluşturuldu.")
        except Exception as e:
            print(f"bir hata oluştu: {e}")
            return None
    def get_employee(self, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            print(employee.full_name, employee.email, employee.annual_salary, employee.tenure_in_years)
            return employee
        except Employee.DoesNotExist:
            print(f"belirtilen {employee_id} mevcut değil.")
            return None
    def get_all_employees(self):
        try:
            employees = Employee.objects.all()
            for emp in employees:
                print(emp.full_name, emp.email, emp.annual_salary, emp.tenure_in_years)
            return employees
        except Exception as e:
            print(f"bir hata oluştu: {e}")
            return None
    def update_salary(self,employee_id, new_salary):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.salary = new_salary
            employee.save()
            print(f"Employee '{employee.full_name}' güncellendi {new_salary}.")
        except Employee.DoesNotExist:
            print(f"belirtilen {employee_id} mevcut değil.")
        except Exception as e:
            print(f"bir hata oluştu: {e}")
    def delete_employee(self, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            print(f"Employee '{employee.full_name}' başarıyla silindi.")
        except Employee.DoesNotExist:
            print(f"belirtilen {employee_id} mevcut değil.")
        except Exception as e:
            print(f"bir hata oluştu: {e}")


