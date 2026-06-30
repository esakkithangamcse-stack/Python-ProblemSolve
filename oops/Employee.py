class Employee:
    class_company = "Cognizent Technologies"
    
    def __init__(self, id, name, dept, salary):
        self.emp_id = id
        self.name = name
        self.dept = dept
        self.salary = salary

    def get_emp_details(self):
        print(f"Emp_ID: {self.emp_id}, Name: {self.name}, Dept: {self.dept}, Salary: {self.salary}")
    
    @classmethod
    def fetch_company_details(cls):
        print(f"Company name: {cls.class_company}")

    @classmethod
    def update_company_name(cls, new_name):
        cls.class_company = new_name
        print(f"Company name updated to {cls.class_company}")

    def update_emp_dept(self, dept):
        self.dept = dept
        print(f"Department updated to {self.dept}")
    
    def update_emp_salary(self, salary):
        self.salary = salary
        print(f"Salary updated to {self.salary}")

    @staticmethod
    def calculate_annual_salary(monthly_salary):
        annual_salary = monthly_salary * 12
        print(f"Annual salary: {annual_salary}")

emp1 = Employee("E001", "Esakki", "IT", 10000)
emp1.get_emp_details()
emp1.update_emp_dept("NON-IT")
emp1.get_emp_details()
emp1.update_emp_salary(15000)
emp1.get_emp_details()
emp1.calculate_annual_salary(15000)

Employee.fetch_company_details()
Employee.update_company_name("Espire Technologies India")
Employee.fetch_company_details()