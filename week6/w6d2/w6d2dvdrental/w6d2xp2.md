SELECT * FROM customer;

SELECT CONCAT(first_name,' ',last_name) as full_name from customer
xxx||' '||YYY >> will concat 2 strings 






-- SELECT * FROM customer;
-- SELECT first_name||' '||last_name as full_name from customer


-- SELECT DISTINCT create_date FROM customer


-- SELECT * FROM customer ORDER BY first_name

-- SELECT film id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate 

-- SELECT address, district, phone FROM address WHERE district= 'Texas'

-- SELECT * FROM film WHERE film_id in (15, 150);

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE '%oney%'  

-- SELECT title, rental_rate as price  FROM film ORDER BY rental_rate asc
-- SELECT title, rental_rate as price  FROM film ORDER BY rental_rate asc LIMIT 10

-- SELECT title, rental_rate as price  FROM film ORDER BY rental_rate asc OFFSET 10 ROWS FETCH FIRST 10 ROWS ONLY 

-- SELECT p.amount, p.payment_date, c.customer_id FROM customer c 
-- FULL JOIN payment p
-- ON p.customer_id = c.customer_id 
-- ORDER BY c.customer_id asc


-- SELECT SUM(p.amount), c.customer_id FROM customer c 
-- FULL JOIN payment p
-- ON p.customer_id = c.customer_id 
-- GROUP BY c.customer_id
-- ORDER BY c.customer_id asc



--  SELECT f.title FROM film f WHERE f.film_id not in (SELECT film_id FROM inventory) 
 
 
-- SELECT c.city, ctr.country FROM country ctr
-- INNER JOIN city c 
-- ON ctr.country_id = c.country_id
-- ORDER BY city;

-- SELECT c.customer_id, c.first_name||' '||c.last_name, p.amount, p.payment_date p.staff_id 
-- FROM 

