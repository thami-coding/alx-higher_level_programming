-- lists the number of records with the
-- same score in the table second_table of the database hbtn_0c_0
-- lists the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table 
GROUP BY score
HAVING COUNT(score) > 0
ORDER BY number DESC;