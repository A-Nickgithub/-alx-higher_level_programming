-- This SQL script retrieves the maximum temperature recorded for each state from the "temperatures" table in the database "hbtn_0c_0", ordering the results by state name.
SELECT state, MAX(temperature) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
