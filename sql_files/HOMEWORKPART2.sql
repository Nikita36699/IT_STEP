CREATE TABLE FRUIT_VEGGIES(
	ID_ITEM SERIAL PRIMARY KEY,
	NAME_ITEM VARCHAR(50),
	TYPE_ITEM VARCHAR(20),
	COLOR  VARCHAR(30),
	CALORIES INT,
	DESCRIPTION VARCHAR(300)
);


INSERT INTO FRUIT_VEGGIES (NAME_ITEM, TYPE_ITEM, COLOR, CALORIES, DESCRIPTION) VALUES
('Яблуко', 'фрукт', 'червоний', 52, 'Соковитий солодкий фрукт.'),
('Банан', 'фрукт', 'жовтий', 96, 'Поживний тропічний фрукт.'),
('Морква', 'овоч', 'помаранчевий', 41, 'Коренеплід, багатий на вітамін A.'),
('Огірок', 'овоч', 'зелений', 16, 'Свіжий овоч для салатів.'),
('Виноград', 'фрукт', 'зелений', 69, 'Солодкі ягоди, що ростуть гронами.');


--■ Відображення всієї інформації з таблиці овочів та фруктів;
SELECT *
FROM  FRUIT_VEGGIES;

--Відображення усіх овочів:
SELECT *
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'овоч';

--■ Відображення усіх фруктів;
SELECT *
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'фрукт';


--■ Відображення усіх назв овочів та фруктів;
SELECT NAME_ITEM 
FROM FRUIT_VEGGIES;


--■ Відображення усіх кольорів. Кольори мають бути унікальними;
SELECT DISTINCT COLOR
FROM FRUIT_VEGGIES;



--■ Відображення фруктів певного кольору;
SELECT *
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'фрукт' AND COLOR = 'зелений';


--■ Відображення овочів певного кольору.
SELECT *
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'овоч' AND COLOR = 'зелений';




