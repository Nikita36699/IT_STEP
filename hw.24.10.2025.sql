DROP TABLE IF EXISTS DEPARTMENTS CASCADE;
DROP TABLE IF EXISTS FACULTIES CASCADE;
DROP TABLE IF EXISTS GROUPS CASCADE;
DROP TABLE IF EXISTS TEACHERS CASCADE;




-- ФАКУЛЬТЕТИ
CREATE TABLE FACULTIES (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
    FINANCING DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (FINANCING >= 0)
);


-- ФАКУЛЬТЕТИ
INSERT INTO FACULTIES (NAME, FINANCING) VALUES
('ІНФОРМАТИКИ', 500000),
('МЕДИЦИНИ', 750000),
('ЕКОНОМІКИ', 300000);

-- КАФЕДРИ
CREATE TABLE DEPARTMENTS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
    FINANCING DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (FINANCING >= 0),
    FACULTYID INT NOT NULL REFERENCES FACULTIES(ID)
);


INSERT INTO DEPARTMENTS (NAME, FINANCING, FACULTYID) VALUES
('КІБЕРБЕЗПЕКА', 150000, 1),
('ПРОГРАМУВАННЯ', 200000, 1),
('АНАТОМІЯ', 250000, 2),
('МІКРОБІОЛОГІЯ', 300000, 2),
('ФІНАНСИ', 100000, 3);


-- ВИКЛАДАЧІ
CREATE TABLE TEACHERS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> ''),
    SALARY DECIMAL(10,2) NOT NULL CHECK (SALARY > 0)
);


INSERT INTO TEACHERS (NAME, SURNAME, SALARY) VALUES
('ІВАН', 'ПЕТРЕНКО', 25000),
('ОЛЕНА', 'КОВАЛЕНКО', 28000),
('АНДРІЙ', 'СИДОРЕНКО', 30000),
('СВІТЛАНА', 'МЕЛЬНИК', 32000);



-- КУРАТОРИ
CREATE TABLE CURATORS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> '')
);




INSERT INTO CURATORS (NAME, SURNAME) VALUES
('ІГОР', 'ДАНИЛЮК'),
('ЛІЛІЯ', 'ПОЛІЩУК'),
('ВІКТОР', 'САВЧЕНКО');



-- ПРЕДМЕТИ
CREATE TABLE SUBJECTS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> '')
);


INSERT INTO SUBJECTS (NAME) VALUES
('БАЗИ ДАНИХ'),
('АНАТОМІЯ ЛЮДИНИ'),
('МІКРОЕКОНОМІКА'),
('ПРОГРАМУВАННЯ PYTHON');

-- ЛЕКЦІЇ
CREATE TABLE LECTURES (
    ID SERIAL PRIMARY KEY,
    LECTUREROOM VARCHAR(255) NOT NULL CHECK (LECTUREROOM <> ''),
    SUBJECTID INT NOT NULL REFERENCES SUBJECTS(ID),
    TEACHERID INT NOT NULL REFERENCES TEACHERS(ID)
);


-- ГРУПИ
CREATE TABLE GROUPS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(10) NOT NULL UNIQUE CHECK (NAME <> ''),
    YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5),
    DEPARTMENTID INT NOT NULL REFERENCES DEPARTMENTS(ID)
);


-- ГРУПИ ТА КУРАТОРИ
CREATE TABLE GROUPSCURATORS (
    ID SERIAL PRIMARY KEY,
    CURATORID INT NOT NULL REFERENCES CURATORS(ID),
    GROUPID INT NOT NULL REFERENCES GROUPS(ID)
);



-- ГРУПИ ТА ЛЕКЦІЇ
CREATE TABLE GROUPSLECTURES (
    ID SERIAL PRIMARY KEY,
    GROUPID INT NOT NULL REFERENCES GROUPS(ID),
    LECTUREID INT NOT NULL REFERENCES LECTURES(ID)
);



-- ЛЕКЦІЇ
INSERT INTO LECTURES (LECTUREROOM, SUBJECTID, TEACHERID) VALUES
('АУДИТОРІЯ 101', 1, 1),
('АУДИТОРІЯ 102', 4, 2),
('АУДИТОРІЯ 201', 2, 3),
('АУДИТОРІЯ 301', 3, 4);

-- ГРУПИ
INSERT INTO GROUPS (NAME, YEAR, DEPARTMENTID) VALUES
('ІНФ-11', 1, 2),
('ІНФ-21', 2, 1),
('МЕД-31', 3, 3),
('ЕКО-41', 4, 5);

-- ГРУПИ ТА КУРАТОРИ
INSERT INTO GROUPSCURATORS (CURATORID, GROUPID) VALUES
(1, 1),
(2, 2),
(3, 3);

-- ГРУПИ ТА ЛЕКЦІЇ
INSERT INTO GROUPSLECTURES (GROUPID, LECTUREID) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 4);



--1. Усі можливі пари викладачів і груп
SELECT 
    Teachers.Name AS TeacherName,
    Groups.Name AS GroupName
FROM Teachers
CROSS JOIN Groups;

--6. Назви кафедр і груп, що до них належать
SELECT 
    Departments.Name AS DepartmentName,
    Groups.Name AS GroupName
FROM Departments
JOIN Groups ON Groups.DepartmentId = Departments.Id;

--2 Факультети, фонд кафедр яких > фонду факультету
SELECT DISTINCT f.Name
FROM Faculties f
JOIN Departments d ON d.FacultyId = f.Id
WHERE d.Financing > f.Financing;


--7 Предмети ІВАН ПЕТРЕНКО
SELECT DISTINCT s.Name
FROM Subjects s
JOIN Lectures l ON l.SubjectId = s.Id
JOIN Teachers t ON t.Id = l.TeacherId
WHERE t.NAME = 'ІВАН' AND t.SURNAME = 'ПЕТРЕНКО';


SELECT DISTINCT d.Name
FROM Departments d
JOIN Groups g ON g.DepartmentId = d.Id
JOIN Lectures l ON l.GroupId = g.Id
JOIN Subjects s ON s.Id = l.SubjectId
WHERE s.Name = 'Database Theory';

