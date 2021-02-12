INSERT INTO account (account_id, customer_id, loan_id, service_id, policy_id)
VALUES (5, 5, 5, 5, 5);

ALTER TABLE account ENABLE TRIGGER ALL;

select *
FROM payment

UPDATE maintenance
SET car_id = 3
WHERE service_id = 4
-- -- -- 
2)
SELECT date_created
FROM customer
-- 
3)
SELECT credit_score
FROM customer
WHERE credit_score > 650
-- 
4)
BEGIN;
UPDATE payment SET payment_amount = payment_amount - 100.00
    WHERE payment_id = 1;
COMMIT;
-- 
5)
BEGIN;
UPDATE payment SET payment_amount = payment_amount + late_fee
    WHERE payment_id = 1;
COMMIT;
-- 
6)
SELECT first_name, last_name, payment_amount, due_date
FROM payment
JOIN customer on payment.account_id = customer.account_id
-- 
7)
CREATE VIEW payment_due_view AS
	SELECT payment_amount, due_date
	FROM payment;
-- or 
CREATE VIEW pays AS 
    SELECT payment_amount,due_date
    from payment
    where payment_amount > 300

-- 
8)
SELECT mx_date
FROM maintenance
WHERE service_id = 1
-- 
9)
SELECT first_name,last_name,make,model
from car
JOIN customer on customer.account_id = car.account_id
Where first_name = 'Bill'