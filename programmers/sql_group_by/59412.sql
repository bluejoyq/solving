SELECT HOUR(DATETIME) AS HOUR, COUNT('HOUR') AS 'COUNT' FROM ANIMAL_OUTS GROUP BY HOUR
	HAVING HOUR BETWEEN 9 AND 20 ORDER BY HOUR;