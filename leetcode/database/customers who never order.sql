SELECT name as Customers
FROM Customers
WHERE id NOT IN (select customerId from Orders)