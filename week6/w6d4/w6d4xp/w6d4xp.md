SELECT first_name "First Name" , last_name AS "Last Name" FROM employees 

>>when you want to Alias column >>use " and not '


SELECT department_id FROM employees 
WHERE department_id in (SELECT department_id FROM employees GROUP BY department_id HAVING count(*)=1)

SELECT count(*), e.department_id FROM employees e
GROUP BY department_id
HAVING count(*) = 1 


SELECT * FROM employees ORDER BY first_name desc  

SELECT first_name, last_name, salary, salary * 0.15 PF FROM employees 

SELECT concat(first_name,' ',last_name), salary  FROM employees e ORDER BY salary ASC

SELECT SUM(salary) FROM employees

SELECT MIN(salary), MAX(salary) FROM employees

SELECT AVG(salary) FROM employees

SELECT count(employee_id) FROM employees

SELECT upper(first_name) FROM employees


SELECT SUBSTRING (upper(first_name), 0, 3)  FROM employees;

SELECT LEFT (upper(first_name), 3)  FROM employees




SELECT concat(first_name,' ',last_name) FROM employees 

SELECT first_name FROM employees WHERE first_name LIKE '%[0-9]%' 

SELECT * from employees LIMIT 10 



-----part 2
SELECT first_name, last_name, salary from employees WHERE salary BETWEEN 10000 and 15000


SELECT first_name, last_name, hire_date from employees WHERE hire_date BETWEEN '1987-01-01' AND '1987-12-31'

SELECT first_name from employees WHERE first_name LIKE '%a%e%'


SELECT e.last_name, j.job_title, e.salary FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id 
WHERE job_title NOT LIKE 'Programmer'  
AND job_title NOT LIKE 'Shipping Clerk'
AND salary NOT IN (4500,10000,15000)

SELECT last_name FROM employees WHERE length(last_name) = 6


SELECT last_name FROM employees WHERE last_name LIKE '__e%'


SELECT j.job_title FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id

SELECT * FROM employees WHERE UPPER(last_name) IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')


UPDATE employees 
SET email = 'unavailable'  
WHERE department_id = 110


UPDATE employees  SET email = 'Available' 
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = 'Accounting')  


UPDATE employees SET salary = 8000 WHERE employee_id=105 AND salary < 5000

UPDATE employees 
SET 
salary = salary *1.25 WHERE department_id =40
salary = salary *1.15 WHERE despartment_id =90
salary = salary *1.10 WHERE despartment_id =110
