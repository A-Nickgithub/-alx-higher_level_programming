-- Create a table unique_id with id INT having a default value of 1 and must be unique, and name VARCHAR(256).
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
