SELECT language.name FROM language;

SELECT f.title, f.description, l.name FROM film f
INNER JOIN language l 
ON f.language_id = l.language_id 


SELECT film.title, film.description, language.name FROM film, language 
WHERE film.language_id = language.language_id


SELECT f.title, f.description, l.name FROM film f
FULL JOIN language l 
ON f.language_id = l.language_id 

-- CREATE TABLE customer_review(
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER REFERENCES film (film_id),
-- 	language_id  INTEGER REFERENCES language (language_id),
-- 	title VARCHAR(100) NOT NULL,
-- 	score  SMALLINT NOT NULL,
-- 	review_text  VARCHAR NOT NULL,
-- 	last_update DATE NOT NULL
-- )


alter table customer_review
add constraint film_id
   foreign key (film_id)
   references film(film_id)
   on delete cascade;




INSERT INTO customer_review(film_id, language_id, language_id, title, score, review_text, last_update) 

S (23, 2, 'this a an unknown title', 2, 'I kind of didnt like this as I wasnt sure about what i was looking', '12/09/2020' ),
(123, 2, 'Not sure', 5, 'LOOK inside ', '12/01/2020' )



DELETE FROM film WHERE film_id = 23


-----EX 2


UPDATE film SET 
language_id = 2 WHERE film_id = 1,

language_id = 2 WHERE film_id = 2,
language_id = 2 WHERE film_id = 3


store_id and address_id 
The other tables have to exist other wise it wont accept 


DROP TABLE customer_review
>>no Issues to drop the table



SELECT count(*) FROM rental 
>> 16044


SELECT f.title, f.rental_rate  FROM rental r
INNER JOIN inventory i
ON i.inventory_id = r.inventory_id
INNER JOIN film f 
ON i.film_id = f.film_id
ORDER BY rental_rate desc LIMIT 30 



SELECT f.title, f.description
FROM film f, film_actor fa, actor a 
WHERE f.film_id = fa.film_id 
AND fa.actor_id = a.actor_id 
AND f.description LIKE '%Sumo Wrestler%' 
AND a.first_name||' '||a.last_name LIKE 'Penelope Monroe'
>>PARK CITIZEN



SELECT f.title, f.length, f.rating
FROM film f, film_category fc, category c 
WHERE f.film_id = fc.film_id 
AND fc.category_id = c.category_id 
AND c.name LIKE 'Documentary' 
AND f.rating = 'R'
AND f.length < 60
>>>"Cupboard Sinners"


SELECT f.title, c.First_name||''||c.last_name, f.rental_rate, r.return_date
FROM film f, inventory i, rental r, customer c 
WHERE f.film_id = i.film_id 
AND i.inventory_id = r.inventory_id 
AND c.first_name||' '||c.last_name LIKE  'Matthew%Mahan'
AND r.return_date BETWEEN '07/28/2005' AND '08/01/2005'
AND f.rental_rate > 4
>>many MOVIES is he board in life?



SELECT f.title, f.rental_rate
FROM film f, inventory i, rental r, customer c 
WHERE f.film_id = i.film_id 
AND i.inventory_id = r.inventory_id 
AND c.first_name||' '||c.last_name LIKE  'Matthew%Mahan'
AND f.title LIKE 'boat' OR f.description LIKE 'boat'
AND f.replacement_cost in (SELECT f.replacement_cost FROM film f ORDER BY replacement_cost DESC limit 10);
>>>didnt return me anython (not error)


