-- Question 1 - List the account name with the longest website url.
SELECT name
FROM sqlchallenge1.accounts
ORDER BY length(website) DESC LIMIT 1;
-- Answer: United Continental Holdings

-- Question 2 - How many sales reps have the letter "e" their names.
SELECT COUNT(*)
FROM sqlchallenge1.sales_reps
WHERE name ILIKE '%e%';
-- Answer: 40

-- Question 3 - What is the alphabetically first account name that contains an ampersand ("&")? 
SELECT name
FROM sqlchallenge1.accounts
WHERE name LIKE '%&%'
ORDER BY name;
-- Answer: Air Products & Chemicals

-- Question 4 - What is the id of the sales rep that sold the last order in May 2015.
WITH query1
  AS 
   (SELECT ac.sales_rep_id, o.occurred_at as data 
  FROM sqlchallenge1.orders o

INNER JOIN sqlchallenge1.accounts ac
ON ac.id = o.account_id
WHERE o.occurred_at
BETWEEN '2015/05/01 00:00:00' AND '2015/05/31 23:59:59'
ORDER BY data DESC
LIMIT 1),

query2 AS (
  SELECT * FROM sqlchallenge1.sales_reps
)

SELECT id FROM query1 
INNER JOIN query2
ON query1.sales_rep_id = query2.id
-- Answer: 321760

-- Question 5 - How many Sales Reps represent the Northeast region
SELECT COUNT(*)
FROM sqlchallenge1.sales_reps
WHERE region_id = (SELECT id FROM sqlchallenge1.region WHERE name = 'Northeast');
-- Answer: 21