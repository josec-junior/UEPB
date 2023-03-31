-- Passo 01 - Recuperar o relatório correspondente à cena do crime
SELECT * FROM 'crime_scene_report'
WHERE date = '20180115' AND city = 'SQL City' AND type = 'murder';

-- Passo 02 - Procurar pela primeira testemunha, a qual vive na última casa da Northwestern Dr
SELECT * FROM 'person'
WHERE address_street_name = 'Northwestern Dr'
ORDER BY address_number DESC
LIMIT 1;

-- Passo 03 - Entrevistar a primeira testemunha
SELECT * FROM 'interview'
WHERE person_id = (SELECT id FROM 'person'
WHERE name = "Morty Schapiro");

-- Passo 04 - Procurar quem começa com "48Z" na ficha de inscrição da academia e é membro gold
SELECT * FROM 'get_fit_now_member'
WHERE id LIKE "48Z%" AND membership_status = "gold";

-- Passo 05 - Procurar pelo carro que possui "H42W" na placa
SELECT * FROM 'drivers_license'
WHERE plate_number LIKE "%H42W%" AND gender = 'male';

-- Passo 06 - Procurar pelos donos dos carros que possuem "H42W" na placa
SELECT * FROM 'person'
WHERE license_id IN (SELECT id FROM 'drivers_license'
WHERE plate_number LIKE "%H42W%" AND gender = 'male');

-- Passo 07 - Prender o principal suspeito
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
SELECT value FROM solution;

-- Passo 08 - Interrogar o principal suspeito
SELECT * FROM 'interview'
WHERE person_id IN (SELECT id FROM 'person'
WHERE license_id IN (SELECT id FROM 'drivers_license'
WHERE plate_number LIKE "%H42W%" AND gender = 'male'));

-- Passo 09 - Procurar pela mulher mandante do crime, através das informações divulgadas pelo assassino
SELECT name FROM 'person'
WHERE license_id IN (SELECT id FROM 'drivers_license'
WHERE gender = "female" AND hair_color = "red" AND car_make = "Tesla" AND car_model = "Model S")
AND id IN (SELECT person_id FROM facebook_event_checkin
WHERE event_name LIKE "%SQL Symphony%" AND date LIKE '201712%'
GROUP BY person_id
HAVING COUNT(*) = 3);

-- Passo 10 - Prender a mulher mandante do crime
INSERT INTO solution VALUES (1, 'Miranda Priestly');
SELECT value FROM solution;