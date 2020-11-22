CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	last_name VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	dob DATE Not NULL
)

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	last_name VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	dob DATE Not NULL
);

INSERT INTO students (first_name, last_name, dob)
VALUES 
('Marc', 'Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')),
('Yoan', 'Cohen', TO_DATE('03/12/2010', 'DD/MM/YYYY')),
('Lea',	'Benichou',	TO_DATE('27/07/1987', 'DD/MM/YYYY')),
('David', 'Grez', TO_DATE('14/06/2003', 'DD/MM/YYYY')),
('Omer', 'Simpson', TO_DATE('03/10/1980', 'DD/MM/YYYY')),
('Amelia', 'Dux', TO_DATE('07/04/1996', 'DD/MM/YYYY'))


SELECT * FROM students;
SELECT first_name, last_name FROM students WHERE id = 2;
SELECT first_name, last_name FROM students WHERE first_name = 'Marc' AND last_name ='Benichou';
SELECT first_name, last_name FROM students WHERE first_name = 'Marc' OR last_name ='Benichou';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE 'A%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_';
SELECT * FROM students WHERE id in (1,3);
SELECT * FROM students WHERE dob >= '01/01/2000';


