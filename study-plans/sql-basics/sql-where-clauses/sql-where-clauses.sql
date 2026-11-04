-- Returns: name, salary.
SELECT name,salary from employees
Where salary>70000 and department IN ('Engineering', 'Marketing');