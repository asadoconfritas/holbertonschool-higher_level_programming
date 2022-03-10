-- Cities by States
-- script that lists all cities
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states
ON cities.states_id=states_id
ORDER BY cities.id ASC
