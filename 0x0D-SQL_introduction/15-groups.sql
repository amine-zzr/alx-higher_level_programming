-- Using the GROUP BY clause along with the COUNT() function
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
