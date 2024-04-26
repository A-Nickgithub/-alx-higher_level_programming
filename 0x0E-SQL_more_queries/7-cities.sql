-- scripts creates a database htbn_0d_usa and the table cities on your MySQL server
-- id INT UNIQUE AUTO NOT NULL PK, state_id INT NOT NULL FK that references to id of the states table, name VARCHAR(256) NOT NULL

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL);
