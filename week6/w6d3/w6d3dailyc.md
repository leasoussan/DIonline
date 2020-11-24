DROP TABLE if EXISTS shakes;

CREATE TABLE shake_type (
 	id SERIAL PRIMARY KEY,
	shake_type INTEGER NOT NULL
);

CREATE TABLE fruits (
	id SERIAL PRIMARY KEY,
	fruit VARCHAR(30)
);

CREATE TABLE vegetables (
	id SERIAL PRIMARY KEY,
	vegetable VARCHAR(30) 
);

	
CREATE TABLE extra (
	id SERIAL PRIMARY KEY,
	extra VARCHAR(30) 
);




CREATE TABLE fruits_vegetables (
	id SERIAL primary key,
	fruits INTEGER NOT NULL REFERENCES fruits(id), 
	vegetables INTEGER NOT NULL REFERENCES vegetables(id) 
);

 


	

DROP TABLE if EXISTS customer;

CREATE TABLE customer_order(
	id SERIAL PRIMARY KEY, 
	first_name VARCHAR(30) NOT NULL,
	shake_type INTEGER, 
	fruits_vegetables INTEGER, 
	extra INTEGER,
	note VARCHAR,
	FOREIGN KEY (shake_type) REFERENCES shake_type(id),
	FOREIGN KEY (fruits_vegetables) REFERENCES fruits_vegetables(id),
	FOREIGN KEY (extra) REFERENCES extra(id)
);