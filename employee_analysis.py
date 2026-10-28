import pandas as pd

# 1. Read employee details from the CSV file
df = pd.read_csv('employee.csv')

print("--- 1. Employee Data Loaded Successfully ---")

# 2. Display employee names, departments, and salaries
# (Assuming the columns are named 'Name', 'Department', and 'Salary')
print("\n--- 2. Employee Names, Departments, and Salaries ---")
print(df[['Name', 'Department', 'Salary']])

# 3. Calculate the average salary for each department
print("\n--- 3. Average Salary for Each Department ---")
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)
