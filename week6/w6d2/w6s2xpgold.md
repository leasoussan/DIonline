
SELECT rating, count(rating)  FROM film GROUP BY rating;

SELECT title, rating  FROM film WHERE rating IN ('PG', 'PG-13') order by rating asc;

SELECT title, rating, length, rental_rate  FROM film 
WHERE rating IN ('PG', 'PG-13')
AND length < 120
AND rental_rate < 3 ORDER BY title asc

SELECT * FROM customer;
UPDATE customer SET first_name = 'lola' , last_name = 'ramobo', activebool= false; WHERE id=1




---------------EX2
SELECT * FROM students;

UPDATE students SET dob = '02/11/1998' WHERE last_name = 'Benichou'

UPDATE students SET last_name = 'Guez' WHERE last_name = 'Grez'


DELETE FROM students WHERE first_name='Lea' and last_name = 'Benichou'

SELECT count(*) FROM students;


SELECT count(*) FROM students WHERE dob > '01/01/2000'


ALTER TABLE students ADD COLUMN Math_grade SMALLINT 



UPDATE students set Math_grade= 80 WHERE id=1;


UPDATE students set Math_grade= 90 WHERE id IN (2,4);



UPDATE students set Math_grade= 40 WHERE id=5


SELECT count(math_grade) FROM Students WHERE math_grade > 83



INSERT INTO students (last_name, first_name, dob, math_grade)
VALUES ('Simpson', 'Omer', '1980-10-03', 70)




SELECT last_name, first_name, count(math_grade) total_grade FROM students GROUP BY last_name, first_name


SELECT SUM(math_grade) FROM students
