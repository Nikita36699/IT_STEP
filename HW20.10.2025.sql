-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
CREATE TABLE  DEPARTMENTS(
	ID SERIAL PRIMARY KEY,
	FINANCING INT  NOT NULL CHECK(FINANCING > 0 ) DEFAULT 0,
	NAME VARCHAR(100) NOT NULL UNIQUE CHECK(NAME != '')
);


INSERT INTO Departments (FINANCING, NAME) VALUES
(50000, 'Кафедра математики'),
(40000, 'Кафедра інформатики'),
(30000, 'Кафедра філології'),
(35000, 'Кафедра історії'),
(25000, 'Кафедра економіки');

-- 2️⃣ ФАКУЛЬТЕТИ
CREATE TABLE FACULTIES(
	ID SERIAL PRIMARY KEY,
	DEAN VARCHAR(255) NOT NULL CHECK(DEAN != ''),
	NAME VARCHAR(100) NOT NULL UNIQUE  CHECK(NAME != '')	
);


INSERT INTO FACULTIES (DEAN, NAME) VALUES
('Олександр Петренко', 'Факультет комп’ютерних наук'),
('Марія Іваненко', 'Факультет гуманітарних наук'),
('Ігор Коваленко', 'Факультет природничих наук'),
('Ганна Мельник', 'Факультет економіки'),
('Василь Сидоренко', 'Факультет історії та філософії');


-- 3️⃣ ГРУПИ
CREATE TABLE GROUPS(
    ID SERIAL PRIMARY KEY,
    NAME  VARCHAR(10) NOT NULL UNIQUE CHECK(NAME != ''),
    RATING INT NOT NULL CHECK(RATING BETWEEN 0 AND 5),
    YEAR INT NOT NULL CHECK(YEAR BETWEEN 1 AND 5)
);

INSERT INTO GROUPS (NAME , RATING, YEAR) VALUES
('КН-11', 5, 1),
('КН-21', 4, 2),
('ФІ-31', 3, 3),
('ЕК-22', 4, 2),
('ІС-41', 5, 4),
('ГМ-15', 2, 1),
('ІН-32', 3, 3),
('ІС-25', 5, 2),
('ІТ-14', 4, 1),
('ФЛ-23', 3, 2);


-- 4️⃣ ВИКЛАДАЧІ
CREATE TABLE TEACHERS (
	ID SERIAL PRIMARY KEY,
	EMPLOYMENTDATE DATE NOT NULL CHECK(EMPLOYMENTDATE >= '1990-01-01'),
	ISASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
	ISPROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
	NAME VARCHAR(255) NOT NULL CHECK(NAME != ''),
	POSITION VARCHAR(255) NOT NULL CHECK(POSITION != ''),
	PREMIUM INT NOT NULL CHECK(PREMIUM >= 0) DEFAULT 0,
	SALARY INT NOT NULL CHECK(SALARY > 0),
	SURNAME VARCHAR(255) NOT NULL CHECK(SURNAME != '')
);

INSERT INTO TEACHERS (EMPLOYMENTDATE, ISASSISTANT, ISPROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME) VALUES
('2005-09-01', FALSE, TRUE, 'Олександр', 'Професор', 3000, 20000, 'Петренко'),
('2010-02-15', TRUE, FALSE, 'Ірина', 'Асистент', 1500, 12000, 'Іваненко'),
('2000-10-10', FALSE, TRUE, 'Василь', 'Професор', 2500, 18000, 'Коваль'),
('2015-08-20', FALSE, FALSE, 'Марина', 'Доцент', 2000, 16000, 'Шевченко'),
('2018-03-05', TRUE, FALSE, 'Богдан', 'Асистент', 1000, 11000, 'Мельник'),
('2012-11-12', FALSE, TRUE, 'Світлана', 'Професор', 3000, 19000, 'Кравченко'),
('2020-01-15', TRUE, FALSE, 'Олена', 'Асистент', 800, 10000, 'Романюк'),
('2016-05-01', FALSE, FALSE, 'Дмитро', 'Доцент', 1200, 14000, 'Лисенко'),
('2008-09-01', FALSE, TRUE, 'Юрій', 'Професор', 3500, 22000, 'Гончар'),
('2019-04-10', TRUE, FALSE, 'Аліна', 'Асистент', 900, 9500, 'Бондар');


SELECT * FROM DEPARTMENTS;
SELECT * FROM FACULTIES;
SELECT * FROM GROUPS;
SELECT * FROM TEACHERS;



-- 1. ВИВЕСТИ ТАБЛИЦЮ КАФЕДР, АЛЕ РОЗТАШУВАТИ ЇЇ ПОЛЯ У ЗВОРОТНОМУ ПОРЯДКУ.
SELECT NAME, FINANCING, ID
FROM DEPARTMENTS;

-- 2. ВИВЕСТИ НАЗВИ ГРУП ТА ЇХ РЕЙТИНГИ З УТОЧНЕННЯМИ ДО НАЗВ ПОЛІВ ВІДПОВІДНО ДО НАЗВИ ТАБЛИЦІ.
SELECT NAME AS GROUP_NAME, RATING AS GROUP_RATING
FROM GROUPS;

-- 3. ВИВЕСТИ ДЛЯ ВИКЛАДАЧІВ ЇХ ПРІЗВИЩА, ВІДСОТОК СТАВКИ ПО ВІДНОШЕННЮ ДО НАДБАВКИ 
-- ТА ВІДСОТОК СТАВКИ ПО ВІДНОШЕННЮ ДО ЗАРПЛАТИ (СУМА СТАВКИ ТА НАДБАВКИ).
SELECT 
    SURNAME,
    (SALARY / NULLIF(PREMIUM, 0)) * 100 AS SALARY_TO_PREMIUM_PERCENT,
    (SALARY / (SALARY + PREMIUM)) * 100 AS SALARY_TO_TOTAL_PERCENT
FROM TEACHERS;

-- 5. ВИВЕСТИ ПРІЗВИЩА ПРОФЕСОРІВ, СТАВКА ЯКИХ ПЕРЕВИЩУЄ 1050.
SELECT SURNAME
FROM TEACHERS
WHERE ISPROFESSOR = TRUE AND SALARY > 1050;


-- 13. ВИВЕСТИ ПРІЗВИЩА АСИСТЕНТІВ ІЗ ЗАРПЛАТОЮ (СУМА СТАВКИ ТА НАДБАВКИ) НЕ БІЛЬШЕ 1200.
SELECT SURNAME
FROM TEACHERS
WHERE ISASSISTANT = TRUE 
  AND (SALARY + PREMIUM) <= 1200;

-- 14. ВИВЕСТИ НАЗВИ ГРУП 5-ГО КУРСУ З РЕЙТИНГОМ У ДІАПАЗОНІ ВІД 2 ДО 4.
SELECT NAME
FROM GROUPS
WHERE YEAR = 5 
  AND RATING BETWEEN 2 AND 4;

-- 15. ВИВЕСТИ ПРІЗВИЩА АСИСТЕНТІВ ЗІ СТАВКОЮ МЕНШЕ, НІЖ 550 
-- АБО НАДБАВКОЮ МЕНШЕ, НІЖ 200.
SELECT SURNAME
FROM TEACHERS
WHERE ISASSISTANT = TRUE 
  AND (SALARY < 550 OR PREMIUM < 200);

