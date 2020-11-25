CHANGED DB NAME as it was under the name 'test
>>>CONSOL
SELECT  *
FROM pg_stat_activity
WHERE datname = 'test';


SELECT
    pg_terminate_backend (pid)
FROM
    pg_stat_activity
WHERE
    datname = 'test';


ALTER DATABASE test RENAME TO shikshak;

------------------------------------

ALTER TABLE fruits RENAME TO fruits_stock;


ALTER TABLE vegetables RENAME TO vegetables_stock;


ALTER TABLE extra RENAME TO extra_stock

ALTER TABLE fruits_stock ADD COLUMN stock INTEGER

ALTER TABLE extra_stock ADD COLUMN stock INTEGER;

ALTER TABLE vegetables_stock ADD COLUMN stock INTEGER

INSERT INTO fruits_stock (fruit, stock) 
VALUES
('banana', 20),
('strawberry', 30),
('appels', 20),
('orange',13),
('pear', 23)


INSERT INTO vegetables_stock (vegetable, stock) 
VALUES
('carrot', 20),
('cucumber', 3),
('khale', 10),
('cilantro',23),
('persil', 13)


INSERT INTO extra_stock (extra, stock) 
VALUES
('Crumble', 20),
('nuts', 3),
('peacan', 10),
('coco',23),
('choco', 13),
('protein', 13)


DROP TABLE ingredients

ALTER TABLE customer_order DROP COLUMN fruits_vegetables  
> I want to remove table fruits_vegetable so fk in customer had to be removed as well


ALTER TABLE shake_type ADD COLUMN price FLOAT NOT NULL 


------ALTER TABLE TABLE_NAME ALTER COLUMN column_name TYPE new_data_type >>change the shake to VARCHAR from integer 
but this is a foreign key so I have first to change the foreing key to beon the id


ALTER TABLE shake_type DROP COLUMN shake_type

ALTER TABLE shake_type ADD COLUMN shake VARCHAR(50) NOT NULL





INSERT INTO shake_type (shake_type, price)
VALUES
('small', 12),
('medium', 16),
('large', 20),
('liter', 35)




>>>>>>TBALE WAS DROPPED AS NO NEED
CREATE TABLE inventory (
	id SERIAL PRIMARY KEY, 
	fruits INTEGER REFERENCES fruits_stock (id),
	vegetables INTEGER REFERENCES vegetables_stock (id),
	extra INTEGER REFERENCES extra_stock (id)
	
)


TO GET INVETORY 
SELECT f.fruit, f.stock FROM fruits_stock f WHERE f.stock < 20
UNION 
SELECT v.vegetable, v.stock FROM vegetables_stock v WHERE v.stock < 20
UNION 
SELECT e.extra,  e.stock FROM extra_stock e WHERE e.stock < 20


>>>>>>>>>>>removing price from shake to make a price table 

ALTER TABLE shake_type DROP COLUMN price

CREATE TABLE price (
	id SERIAL PRIMARY KEY,
	product VARCHAR(50) NOT NULL,
	price FLOAT NOT NULL
)

INSERT INTO price (product, price)
VALUES
('s_shake', 14),
('m_shake', 18),
('l_shake', 25),
('xl_shake', 32),
('extra', 3)



>>>Adjusting the customer order table 
ALTER TABLE customer_order ADD COLUMN order_date DATE not NULL

