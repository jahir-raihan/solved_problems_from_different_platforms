
SELECT Department.name as Department, Employee.name as Employee, Salary
FROM Employee JOIN Department ON Employee.DepartmentId = Department.Id
WHERE (Employee.DepartmentId, Salary) IN
  (select departmentId, max(salary)
  from Employee
  group by departmentId)