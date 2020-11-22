SELECT * FROM students;
SELECT * FROM students ORDER BY last_name asc LIMIT 4;
SELECT *  FROM students WHERE dob = (SELECT MIN(dob) FROM students); 
SELECT * FROM students LIMIT 3 OFFSET 2;