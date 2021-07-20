## 중복 테이블 조인 

SELECT emp.Name as Employee 
FROM Employee as emp JOIN Employee as manage ON manage.id = emp.ManagerId
WHERE emp.Salary > manage.Salary
