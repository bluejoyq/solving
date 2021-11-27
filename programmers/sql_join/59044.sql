SELECT AI.NAME, AI.DATETIME FROM ANIMAL_INS AS AI LEFT JOIN ANIMAL_OUTS AS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID WHERE AO.ANIMAL_ID IS NULL ORDER BY AI.DATETIME LIMIT 3;