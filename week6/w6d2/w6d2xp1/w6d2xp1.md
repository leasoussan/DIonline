SELECT * FROM items ORDER BY price asc;
SELECT * FROM items WHERE price >= 80 ORDER BY price desc;
SELECT f_name, l_name FROM customers ORDER BY  f_name asc LIMIT 3 ;
SELECT l_name FROM customers ORDER BY l_name desc; 


CREATE TABLE purchases (
	id SERIAL PRIMARY KEY,
	customer_id SMALLINT NOT NULL,
	item_id SMALLINT NOT NULL,
	
	CONSTRAINT customer_id
	FOREIGN  KEY(customer_id) REFERENCES customers(id),
	CONSTRAINT item_id
	FOREIGN  KEY(item_id) REFERENCES items(id)
	)


    INSERT INTO purchases (customer_id, item_id) 
VALUES (1, NULL); 
ERROR:  null value in column "item_id" of relation "purchases" violates not-null constraint
DETAIL:  Failing row contains (3, 1, null).
SQL state: 23502


INSERT INTO purchases (customer_id, item_id) 
VALUES 
(1, 1),
(2,3),
(1,2),
(2,1),
(3,2) 


SELECT * FROM purchases 