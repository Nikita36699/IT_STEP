SELECT *
FROM FRUIT_VEGGIES;
-- Завдання 1
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
SELECT NAME_ITEM, CALORIES
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'овоч' AND CALORIES < 65;



-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.
SELECT NAME_ITEM, CALORIES
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'фрукт' AND CALORIES BETWEEN 50 AND  70;


-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
SELECT *
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM = 'овоч' AND NAME_ITEM ILIKE '%ОГІРОК%';



-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.
SELECT *
FROM FRUIT_VEGGIES
WHERE DESCRIPTION ILIKE '%ФРУКТ%';




-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору.
SELECT *
FROM FRUIT_VEGGIES
WHERE COLOR ILIKE 'червоний' OR COLOR ILIKE 'зелений';--ЗЕЛЕНИЙ ПОТОМУ-ЧТО В ТАБЛИЦЕ БОЛЬШЕ ИХ 





-- Завдання 2
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.
SELECT  COUNT(*) AS TOTAL_VEGATABLES
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM ILIKE 'овоч';


-- ■ Показати кількість фруктів.
SELECT  COUNT(*) AS TOTAL_FRUITS
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM ILIKE 'фрукт';

-- ■ Показати кількість овочів та фруктів заданого кольору.
SELECT COUNT(*) AS THIS_COLOR_FRUIT_VEGGIES
FROM FRUIT_VEGGIES
WHERE COLOR ILIKE 'ЗЕЛЕНИЙ';



-- ■ Показати кількість овочів та фруктів кожного кольору.
SELECT COUNT(*) AS COUNT_PER_COLOR,COLOR
FROM FRUIT_VEGGIES
GROUP BY  COLOR;


-- ■ Показати мінімальну калорійність овочів та фруктів.
SELECT MIN(CALORIES) AS MIN_CALORIES
FROM FRUIT_VEGGIES;



-- ■ Показати максимальну калорійність овочів та фруктів.
SELECT MAX(CALORIES) AS MAX_CALORIES
FROM FRUIT_VEGGIES;


-- ■ Показати середню калорійність овочів та фруктів.
SELECT AVG(CALORIES) AS AVG_CALORIES
FROM FRUIT_VEGGIES;


-- ■ Показати фрукт з мінімальною калорійністю.
SELECT NAME_ITEM, CALORIES
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM ILIKE 'фрукт'
  AND CALORIES = (
    SELECT MIN(CALORIES)
    FROM FRUIT_VEGGIES
    WHERE TYPE_ITEM ILIKE 'фрукт'
  );


-- ■ Показати фрукт з максимальною калорійністю.
SELECT NAME_ITEM,CALORIES
FROM FRUIT_VEGGIES
WHERE TYPE_ITEM ILIKE 'фрукт'
	AND CALORIES =(
		SELECT MAX(CALORIES)
		FROM FRUIT_VEGGIES
		WHERE TYPE_ITEM ILIKE 'фрукт'
	  );