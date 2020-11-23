CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	price float(10) NOT NULL);
	
	
CREATE TABLE customers (
	id SERIAL,
	f_name VARCHAR(50) NOT NULL,
	l_name VARCHAR(50) NOT NULL)
	
	

INSERT INTO items (name, price) 
VALUES 
('Small Desk', '100' ) ,
('Large Desk', 300),
('Fan', 80)

INSERT INTO customers (fname, lname) 
VALUES 
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson') 


SELECT * from items;
SELECT * from items WHERE price > 80;
SELECT * from items WHERE price < 300;
SELECT * from customers WHERE l_name = 'Smith';
SELECT * from customers WHERE l_name = 'Jones';
SELECT * from customers WHERE f_name != 'Scott';


SELECT * FROM purchases;
SELECT * 
FROM purchases LEFT JOIN customers ON purchases.customer_id = customers.id

LEFT JOIN will show even empty purchases 
RIGH JOIN will leave empty if there is NULL entry 
INNER join will cancel if there is NULL 
OUTER JOIN will show all of the purchases will the empty one -no connectons obliged 


SELECT * 
FROM purchases p 
LEFT JOIN customers c 
ON p.customer_id = c.id WHERE c.id=4

SELECT * 
FROM purchases p 
LEFT JOIN items i
ON p.item_id = i.id WHERE i.name IN ('Large Desk','Small Desk')



 INSERT INTO items (name, price) VALUES ('Hard Drive', 100);

INSERT INTO purchases (customer_id, item_id)
VALUES(3,4)


SELECT c.f_name, c.l_name, i.name FROM purchases p 
RIGHT JOIN customers c 
ON p.customer_id = c.id
LEFT JOIN items i
ON p.item_id = i.id



