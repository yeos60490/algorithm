## 중복된 이메일 출력 

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1
