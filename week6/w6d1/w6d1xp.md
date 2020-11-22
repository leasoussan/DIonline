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