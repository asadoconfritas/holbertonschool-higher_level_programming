-- States table
-- script that creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE (id),
	PRIMARY KEY (id)
	FOREIGN KEY (state_id)
	REFERENCES states (id))
