-- Temperatures #2
-- script that displays the max temperature of each state
SELECT city, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3