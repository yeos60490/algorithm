## Person 기준으로 출력 -> left join

SELECT FirstName, LastName, City, State
FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;
