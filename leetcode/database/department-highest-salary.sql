## WHERE 절 () 중요

SELECT Dep.Name as Department, Emp.Name as Employee, Salary
FROM Employee as Emp JOIN Department as Dep ON Emp.DepartmentId = Dep.Id
WHERE (DepartmentId, Salary) IN (
    SELECT DepartmentId, MAX(Salary) FROM Employee GROUP BY DepartmentId
)
