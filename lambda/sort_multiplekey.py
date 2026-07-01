employees = [
    {"name": "Arun", "dept": "IT", "salary": 90000},
    {"name": "Bala", "dept": "HR", "salary": 70000},
    {"name": "Charu", "dept": "IT", "salary": 120000},
    {"name": "Devi", "dept": "HR", "salary": 85000},
]
#sort the employees based on dept and then salary in descending order
print(sorted(employees, key=lambda employee: (employee["dept"], -employee["salary"])))

#find the employee with the highest salary
print(max(employees, key=lambda employee: employee["salary"]))

#find the employee with the lowest salary
print(min(employees, key=lambda employee: employee["salary"]))

#find the employee with the highest salary in HR dept
print(max(employees, key=lambda employee: employee["salary"] if employee["dept"] == "HR" else 0))

#find the second highest salary
print(sorted(employees, key=lambda employee: employee["salary"], reverse=True)[1])

# --- Advanced Interview Approaches (12-Year Experience Level) ---

# 1. Custom Priority Sorting (Business Logic Mapping)
# Scenario: Sort by a specific department priority (not alphabetical), then by salary descending.
dept_priority = {"IT": 1, "HR": 2} # IT comes before HR regardless of alphabet
print("\n1. Sorted by custom dept priority and salary desc:")
print(sorted(employees, key=lambda emp: (dept_priority.get(emp["dept"], 99), -emp["salary"])))

# 2. Resilient Sorting (Handling Missing / Messy Data)
# Scenario: An API returns an employee with a missing/None salary. Standard sorting will crash (TypeError).
messy_employees = employees + [{"name": "Eve", "dept": "IT", "salary": None}]
print("\n2. Resilient Sort handling None values (None placed at the end):")
# Use a tuple (is_none, value) to ensure None salaries go to the bottom without crashing
print(sorted(messy_employees, key=lambda emp: (emp["dept"], emp["salary"] is None, -(emp["salary"] or 0))))

# 3. High-Performance Sorting (Operator Module)
# Scenario: Processing millions of records. itemgetter is implemented in C and is faster than a lambda.
from operator import itemgetter
print("\n3. High-performance sort by dept, then name using operator.itemgetter:")
print(sorted(employees, key=itemgetter("dept", "name")))

# 4. Algorithmic Efficiency for Top N Elements (heapq)
# Scenario: Find the Top 2 highest paid employees in a list of 10 million.
# Sorting the whole list is O(N log N). Using heapq is O(N log K), which is much faster.
import heapq
print("\n4. Top 2 highest paid employees (Optimized O(N log K) approach):")
print(heapq.nlargest(2, employees, key=lambda emp: emp["salary"]))
