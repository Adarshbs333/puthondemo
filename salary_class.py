class salary:
    def __init__(self,n):
        self.basic_sal=n

class allowance(salary):
    def __init__(self, n):
        super().__init__(n)  # Initialize the base class with basic salary
        s_allowance = {"HRA": 0.2, "DA": 0.3, "TA": 0.4}
        self.total_allowance = 0
        for i in s_allowance:
            self.total_allowance += s_allowance[i] * self.basic_sal


class deduction(salary):
    def __init__(self, n):
        super().__init__(n)  # Initialize the base class with basic salary
        self.s_deductions = {"pf": 0.5, "insurance": 5000}
        self.total_deductions = 0
        for i in self.s_deductions.values():
            if type(i) is not int:
                self.total_deductions += i * self.basic_sal
            else:
                self.total_deductions += i

class salary_calc(allowance, deduction):
    def __init__(self, n):
        super().__init__(n)  # Initialize the base class with basic salary
        self.total_salary = self.basic_sal + self.total_allowance - self.total_deductions

employee=salary_calc(25000)
print(employee.total_allowance)
print(employee.total_deductions)
print(employee.total_salary)

