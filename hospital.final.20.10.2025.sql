DROP TABLE IF EXISTS VACATIONS CASCADE;
DROP TABLE IF EXISTS DONATIONS CASCADE;
DROP TABLE IF EXISTS SPONSORS CASCADE;
DROP TABLE IF EXISTS DOCTORSSPECIALIZATIONS CASCADE;
DROP TABLE IF EXISTS SPECIALIZATION CASCADE;
DROP TABLE IF EXISTS WARDS CASCADE;
DROP TABLE IF EXISTS EXAMINATIONS CASCADE;
DROP TABLE IF EXISTS DOCTORS CASCADE;
DROP TABLE IF EXISTS DISEASES CASCADE;
DROP TABLE IF EXISTS DEPARTAMENTS CASCADE;


-- Таблица Departments
CREATE TABLE DEPARTMENTS (
  ID SERIAL PRIMARY KEY,
  BUILDING INT NOT NULL CHECK(BUILDING BETWEEN 1 AND 5),
  FINANCING INT NOT NULL CHECK(FINANCING >= 0),
  NAME VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME)
VALUES
  (1, 150000, 'Кардиология'),
  (2, 120000, 'Неврология'),
  (3, 180000, 'Хирургия'),
  (4, 95000, 'Педиатрия'),
  (5, 110000, 'Травматология'),
  (2, 130000, 'Онкология'),
  (3, 160000, 'Офтальмология');


-- Таблица Diseases
CREATE TABLE DISEASES (
  ID SERIAL PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL UNIQUE CHECK(NAME != ''),
  SEVERITY INT NOT NULL CHECK(SEVERITY >= 1) DEFAULT 1
);

INSERT INTO DISEASES (NAME, SEVERITY)
VALUES
  ('Грипп', 2),
  ('Пневмония', 4),
  ('Мигрень', 2),
  ('Инфаркт миокарда', 5),
  ('Перелом кости', 3),
  ('Диабет', 4),
  ('Астма', 3),
  ('Гипертония', 3),
  ('Гастрит', 2),
  ('Язва желудка', 4),
  ('Артрит', 3),
  ('Аппендицит', 4),
  ('Ожирение', 2),
  ('Рак лёгких', 5),
  ('Депрессия', 3),
  ('Анемия', 2),
  ('Гепатит B', 4),
  ('Псориаз', 2),
  ('Коронавирусная инфекция', 4),
  ('Инсульт', 5);


-- Таблица Doctors
CREATE TABLE DOCTORS (
  ID SERIAL PRIMARY KEY,
  NAME VARCHAR(255) NOT NULL CHECK(NAME != ''),
  SURNAME VARCHAR(255) NOT NULL CHECK(SURNAME != ''),
  PHONE CHAR(10),
  SALARY INT NOT NULL CHECK(SALARY > 0),
  PREMIUM INT NOT NULL DEFAULT 0 CHECK(PREMIUM >= 0)
);

INSERT INTO DOCTORS (NAME, SURNAME, PHONE, SALARY)
VALUES
  ('Алексей', 'Иванов', '9001234567', 85000),
  ('Мария', 'Петрова', '9002345678', 92000),
  ('Дмитрий', 'Сидоров', '9003456789', 87000),
  ('Ольга', 'Кузнецова', '9004567890', 94000),
  ('Игорь', 'Смирнов', '9005678901', 88000),
  ('Анна', 'Волкова', '9006789012', 96000),
  ('Сергей', 'Новиков', '9007890123', 91000),
  ('Елена', 'Федорова', '9008901234', 97000);

-- Таблица Examinations
CREATE TABLE EXAMINATIONS (
  ID SERIAL PRIMARY KEY,
  DAYOFWEEK INT NOT NULL CHECK(DAYOFWEEK BETWEEN 1 AND 7),
  STARTTIME TIME NOT NULL CHECK(STARTTIME BETWEEN '08:00' AND '18:00'),
  ENDTIME TIME NOT NULL CHECK(ENDTIME > STARTTIME),
  NAME VARCHAR(100) NOT NULL UNIQUE CHECK(NAME != '')
);

INSERT INTO EXAMINATIONS (DAYOFWEEK, STARTTIME, ENDTIME, NAME)
VALUES
  (1, '08:00', '08:30', 'Общий осмотр'),
  (1, '08:45', '09:15', 'Измерение давления'),
  (1, '09:30', '10:00', 'Снятие ЭКГ'),
  (2, '08:00', '08:40', 'Рентген грудной клетки');

-- Таблица Wards
CREATE TABLE WARDS (
  ID SERIAL PRIMARY KEY,
  DEPARTMENT_ID INT NOT NULL REFERENCES DEPARTMENTS(ID),
  FLOOR INT NOT NULL CHECK(FLOOR >= 1),
  NAME VARCHAR(20) NOT NULL UNIQUE CHECK(NAME != '')
);

INSERT INTO WARDS (DEPARTMENT_ID, FLOOR, NAME)
VALUES
  (1, 1, 'Палата №101'),
  (1, 2, 'Палата №102'),
  (2, 1, 'Палата №201'),
  (2, 2, 'Палата №202');

-- Таблица Specializations
CREATE TABLE SPECIALIZATIONS (
  ID SERIAL PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL UNIQUE CHECK(NAME != '')
);

INSERT INTO SPECIALIZATIONS (NAME)
VALUES ('Терапевт'), ('Хирург'), ('Кардиолог');

-- Таблица DoctorsSpecializations
CREATE TABLE DOCTORSPECIALIZATIONS (
  ID SERIAL PRIMARY KEY,
  DOCTORID INT NOT NULL REFERENCES DOCTORS(ID),
  SPECIALIZATIONID INT NOT NULL REFERENCES SPECIALIZATIONS(ID)
);

INSERT INTO DOCTORSPECIALIZATIONS (DOCTORID, SPECIALIZATIONID)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);

-- Таблица Sponsors
CREATE TABLE SPONSORS (
  ID SERIAL PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL UNIQUE CHECK(NAME != '')
);

INSERT INTO SPONSORS (NAME)
VALUES ('Umbrella Corporation'), ('Wayne Enterprises');


-- Таблица Donations
CREATE TABLE DONATIONS (
  ID SERIAL PRIMARY KEY,
  AMOUNT INT NOT NULL CHECK(AMOUNT > 0),
  DATE DATE NOT NULL DEFAULT CURRENT_DATE,
  DEPARTMENTID INT NOT NULL REFERENCES DEPARTMENTS(ID),
  SPONSORID INT NOT NULL REFERENCES SPONSORS(ID)
);

INSERT INTO DONATIONS (AMOUNT, DEPARTMENTID, SPONSORID)
VALUES
  (150000, 1, 1),
  (80000, 2, 2);

-- Таблица Vacations

CREATE TABLE VACATIONS (
  ID SERIAL PRIMARY KEY,
  DOCTORID INT NOT NULL REFERENCES DOCTORS(ID),
  STARTDATE DATE NOT NULL,
  ENDDATE DATE NOT NULL CHECK(ENDDATE > STARTDATE)
);

INSERT INTO VACATIONS (DOCTORID, STARTDATE, ENDDATE)
VALUES
  (1, '2025-10-01', '2025-10-10'),
  (2, '2025-11-05', '2025-11-15');

-- 1. Добавление новых колонок в существующие таблицы
ALTER TABLE EXAMINATIONS ADD COLUMN DEPARTMENTID INT REFERENCES DEPARTMENTS(ID);
ALTER TABLE EXAMINATIONS ADD COLUMN DISEASEID INT REFERENCES DISEASES(ID);
ALTER TABLE DOCTORS ADD COLUMN DEPARTMENTID INT REFERENCES DEPARTMENTS(ID);

-- 2. Создание таблицы для связи докторов с обследованиями
CREATE TABLE DOCTORSEXAMINATIONS (
  ID SERIAL PRIMARY KEY,
  DOCTORID INT NOT NULL REFERENCES DOCTORS(ID),
  EXAMINATIONID INT NOT NULL REFERENCES EXAMINATIONS(ID)
);

-- 1. Повні імена лікарів та їх спеціалізації
SELECT d.NAME || ' ' || d.SURNAME AS FullName, s.NAME AS Specialization
FROM DOCTORS d
JOIN DOCTORSSPECIALIZATIONS ds ON d.ID = ds.DOCTORID
JOIN SPECIALIZATIONS s ON ds.SPECIALIZATIONID = s.ID;

-- 2. Прізвища та зарплати (ставка + надбавка) лікарів, які не перебувають у відпустці
SELECT d.SURNAME, (d.SALARY + d.PREMIUM) AS TotalSalary
FROM DOCTORS d
LEFT JOIN VACATIONS v ON d.ID = v.DOCTORID
WHERE v.ID IS NULL;

-- 3. Назви палат, які знаходяться у відділенні «Intensive Treatment»
SELECT w.NAME AS WardName
FROM WARDS w
JOIN DEPARTMENTS dep ON w.DEPARTMENT_ID = dep.ID
WHERE dep.NAME = 'Intensive Treatment';

-- 4. Назви відділень без повторень, які спонсоруються компанією «Umbrella Corporation»
SELECT DISTINCT dep.NAME AS Department
FROM DONATIONS don
JOIN DEPARTMENTS dep ON don.DEPARTMENTID = dep.ID
JOIN SPONSORS sp ON don.SPONSORID = sp.ID
WHERE sp.NAME = 'Umbrella Corporation';

-- 5. Всі пожертвування за останній місяць: відділення, спонсор, сума, дата
SELECT dep.NAME AS Department, sp.NAME AS Sponsor, don.AMOUNT, don.DATE
FROM DONATIONS don
JOIN DEPARTMENTS dep ON don.DEPARTMENTID = dep.ID
JOIN SPONSORS sp ON don.SPONSORID = sp.ID
WHERE don.DATE >= CURRENT_DATE - INTERVAL '1 month';

-- 6. Прізвища лікарів із зазначенням відділень, де проводять обстеження у будні дні
SELECT DISTINCT d.SURNAME, dep.NAME AS Department
FROM DOCTORS d
JOIN DOCTORSEXAMINATIONS de ON d.ID = de.DOCTORID
JOIN EXAMINATIONS e ON de.EXAMINATIONID = e.ID
JOIN DEPARTMENTS dep ON e.DEPARTMENTID = dep.ID
WHERE e.DAYOFWEEK BETWEEN 1 AND 5
  AND dep.NAME IN ('Кардиология', 'Неврология', 'Хирургия');  -- заменяем на существующие отделения

-- 7. Назви відділень, які отримували пожертвування понад 100000, із зазначенням їх лікарів
SELECT DISTINCT dep.NAME AS Department, d.SURNAME AS Doctor
FROM DONATIONS don
JOIN DEPARTMENTS dep ON don.DEPARTMENTID = dep.ID
JOIN DOCTORS d ON d.DEPARTMENTID = dep.ID
WHERE don.AMOUNT > 100000
  AND dep.NAME IN ('Кардиология', 'Хирургия', 'Офтальмология');  -- существующие отделения

---- 8. Назви відділень, в яких лікарі не отримують надбавки
SELECT DISTINCT dep.NAME AS Department
FROM DOCTORS d
JOIN DEPARTMENTS dep ON d.DEPARTMENTID = dep.ID
WHERE d.PREMIUM = 0;  -- если есть хотя бы один доктор с Premium=0


-- 9. Назви відділень і назви захворювань, обстеження з яких проводили
SELECT DISTINCT dep.NAME AS Department, dis.NAME AS Disease
FROM EXAMINATIONS e
JOIN DEPARTMENTS dep ON e.DEPARTMENTID = dep.ID
JOIN DOCTORSEXAMINATIONS de ON e.ID = de.EXAMINATIONID
JOIN DOCTORS d ON de.DOCTORID = d.ID
JOIN DISEASES dis ON e.DISEASEID = dis.ID
WHERE dep.NAME IN ('Кардиология', 'Неврология', 'Хирургия');  -- существующие отделения

