-- SHOW ALL 
SELECT *
FROM ANIMALS;

-- ДОБАВИТИ СТОВПЧИК ДО ІСНУЮЧУЮЧИ ТАБЛИЦІ 
-- СТОВПЧИК З ДАТОЮ  ВАКЦИНАЦІЇ
ALTER TABLE ANIMALS
ADD COLUMN LAST_VACCINE DATE DEFAULT '2025-10-11';


--В SELECT МОЖУТЬ БУТИ ВИРАЗИ(МАТЕМАТИЧНІ І НЕ ТІЛЬКИ)
SELECT 10*AGE+5 AS "RESULT", AGE+ANIMAL_ID "AGE + ID(НАЗВА СТОВПИЧИКА С ПРОПУСКОМ)"
FROM ANIMALS;

SELECT LOWER(BREED) AS BREED , UPPER(COLOR) AS COLOR
FROM ANIMALS;

--РЕГУЛЯРНІ ВИРАЗИ
-- МОВА ШАБЛОВНІВ ДЛЯ STR РЯДКІ (ПОЧИНАЕТЬСЯ З ....., МІСТИТЬ......, НЕ МЕНШЕ.....,РАЗІВ, РЯДКИ ТИПУ DDDD-DD-DD )
-- _ -- ДОВІЛЬНИЙ СИМВОЛ
-- % -- ДОВІЛЬНА КІЛЬКІСТЬ ДОВІЛЬНИХ СИМВОЛІВ(ВКЛЮЧНО З 0)

___ -- РЯДОК ДОВЖИНИ 3 СИМЛОВА
A___ -- РЯДОК ДОВЖИНИ 4, ПОЧИНАЕТЬСЯ НА А 
A% -- ЛЮБОЙ РЯДОК КОТРИЙ ПОЧИНАЕТЬСЯ НА А
%А --ЛЮБОЙ РЯДОК КОТРИЙ ЗАКІНЧУЕТЬСЯ НА А
%А% -- РЯДОК В ЯКОМУ Є ЛІТЕРА А

-- ЗАСТОСУВАТИМ ШАБЛОН МОЖНО ЧЕРЕЗ ОПЕРАТОР LIKE 

SELECT *
FROM ANIMALS
WHERE BREED LIKE '___'; -- ПОРОДА З 3 ЛІТЕР 


SELECT *
FROM ANIMALS
WHERE COLOR LIKE '%і%'; -- КОЛІР МІСТИТЬ ЛІТЕРУ І 

SELECT *
FROM ANIMALS
WHERE COLOR ILIKE '%і%'; -- ШАБЛОН НЕ ЧУТЛИВИЙ ДО РЕГІСТРУ 


--Робота з датою 
-- як давно вакцинувалась 

SELECT CURRENT_DATE - LAST_VACCINE
FROM ANIMALS;

--ТЕЖ САМЕ ЧЕРЕЗ ФУНКЦІЮ AGE 
SELECT AGE(LAST_VACCINE)
FROM ANIMALS;

--ЯКОГО МІСЯЦА ВІДБУЛАСЬ ВАКЦИНАЦІЯ
SELECT LAST_VACCINE, EXTRACT(MONTH FROM LAST_VACCINE ) AS "MONTH"
FROM ANIMALS;

--КОЛИ НАСТУПНА ВАКЦИНАЦІЯ ЯКЩО ТРЕБА РОБИТИ ЧЕРЕЗ ПІВРОКА
SELECT LAST_VACCINE, LAST_VACCINE + INTERVAL '6 MONTHS' AS NEXT_VACCINE
FROM ANIMALS;


-- ГРУПУВАННЯ 
--РОЗДІЛИТИ ДАННІ НА ПЕВНІ СТОВПЧИКИ
-- РОЗБИТТЯ ДАННИХ НА ГРУППИ ПО ОДНОМУ СТОВПЧИКУ ТА ОБРАХУНОК ПЕВНИХ ХАРАКТЕРИСТИК ПО ІНШОМУ СТОВПЧИКУ 

--КІЛ-ТЬ ТВАРИН КОЖНОГО ТИПУ 
SELECT BREED, COUNT(*) -- КІЛЬКІСТЬ РЯДКІВ У КОЖНІЙ ГРУППІ 
FROM ANIMALS
GROUP BY BREED; -- ЗГРУПУВАТИ ПО ПОРОДІ


SELECT LOWER(BREED), COUNT(*) -- КІЛЬКІСТЬ РЯДКІВ У КОЖНІЙ ГРУППІ 
FROM ANIMALS
GROUP BY LOWER(BREED);

-- АГРЕГАТНА ФУНКЦІЯ -- ФУНКЦІЯ ЯКА ОТРИМУЄ БАГАТО ПАРАМЕТРІВ А ПОВЕРТАЄ ОДИН РЕЗУЛЬТ
--ПРИКЛАДИ SUM,MIN,MAX,AVG,COUNT

--ДЛЯ КОЖНОГО ТИПУ ТВАРИН ВИВЕСТИ КІЛЬКІСТЬ МИНІМАЛЬНИЙ МАКС И АВГ ВІК

SELECT BREED, MIN(AGE),MAX(AGE), AVG(AGE)
FROM ANIMALS 
GROUP  BY BREED;


