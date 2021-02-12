SELECT amount
FROM payment
WHERE amount > 5.00
-- 
SELECT first_name
from actor
WHERE first_name LIKE 'P%'
-- 
SELECT DISTINCT district
FROM address
-- 
SELECT *
FROM film
WHERE rating = 'R' AND replacement_cost > 5 AND replacement_Cost < 15
-- 
SELECT *
FROM film
WHERE title LIKE '%Truman%'
-- 
SELECT amount
FROM payment
WHERE amount > 7.99
-- 
SELECT first_name
FROM actor
WHERE first_name LIKE 'D__%'
-- 
SELECT DISTINCT name
from category
GROUP BY category_id
-- 
SELECT DISTINCT store_id
FROM store
--
SELECT *
FROM payment
ORDER BY payment_date DESC
-- 
SELECT *
FROM payment
WHERE amount = 0
--
SELECT SUM(amount)
From payment
WHERE staff_id = 2
-- 
SELECT SUM(amount)
from payment
WHERE customer_id = 75
-- 
#6
-- 
SELECT SUM(amount)
FROM payment
WHERE staff_id = 2
-- 
SELECT DISTINCT count(rating)
FROM film
WHERE rating = 'R' 
-- 
SELECT *
FROM film
-- SELECT SUM(rental_duration)
-- FROM film
-- WHERE rating = 'G'
