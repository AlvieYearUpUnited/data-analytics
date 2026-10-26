USE northwind;

/*
a) What is the name of the table that holds the items Northwind sells?
	Anwer: 'products' is the name of the table that holds the items Northwind sells.
    
b) What is the name of the table that holds the types/categories of the items?
Northwind sells?
	Answer: 'categories' is the name of the table that holds the types/categories of the items Northwind sells.
*/

SELECT * FROM employees;

-- 5a) Margaret Peacock

SELECT * FROM products;
-- 6a) 77 records. Query -> Limit Rows -> Limit to 10 rows
-- 6b) Add "LIMIT 10" to the script, before semicolon. I found this answer by googling. 

SELECT * FROM categories;
-- 7c) The category id of seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;





