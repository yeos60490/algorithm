## 값이 없으면 NULL 로 리턴해야한다
## -> ORDER BY, LIMIT 말고 MAX 사용

SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
