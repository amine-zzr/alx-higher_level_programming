-- Using a SELECT statement with a WHERE clause to filter out
-- rows where the name value is empty or NULL. 
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
