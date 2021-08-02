## 1. 최댓값 구하기
SELECT MAX(DATETIME) as '시간' FROM ANIMAL_INS

## 2. 최솟값 구하기
SELECT MIN(DATETIME) as '시간' FROM ANIMAL_INS

## 3. 동물 수 구하기
SELECT COUNT(*) as 'count' FROM ANIMAL_INS

## 4. 중복 제거하기
SELECT COUNT(DISTINCT NAME) as 'count' FROM ANIMAL_INS

