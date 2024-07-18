SHOW DATABASES;
CREATE DATABASE MarketMinds;

USE MarketMinds;
SHOW TABLES;

CREATE TABLE stock_breaking_info (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    stock_code VARCHAR(10) NOT NULL,
    release_date VARCHAR(10) NOT NULL,
    event_date VARCHAR(10) NOT NULL,
    title VARCHAR(200) NOT NULL,
	content VARCHAR(10000) NOT NULL
);

ALTER TABLE stock_breaking_info CHANGE name stock_name VARCHAR(30) NOT NULL;
SELECT * FROM stock_breaking_info;
DESCRIBE stock_breaking_info;