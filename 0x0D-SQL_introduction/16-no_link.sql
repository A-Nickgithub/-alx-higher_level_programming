-- List all records from the 'second_table' of the 'hbtn_0c_0' database with non-null name values, ordered by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
