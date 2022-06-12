-- lists all cities contained in database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER by cities.id ASC;
