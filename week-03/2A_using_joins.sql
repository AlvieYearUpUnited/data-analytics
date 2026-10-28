USE northwind;

-- 1. Create a single query to list the product id, product name, unit price and category
--    name of all products. Order by category name and within that, by product name.

SELECT products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName
FROM products
JOIN categories ON categories.CategoryID = products.CategoryID
ORDER BY CategoryName, ProductName;

-- 2. Create a single query to list the product id, product name, unit price and supplier
--    name of all products that cost more than $75. Order by product name.

SELECT products.ProductID, products.ProductName, products.UnitPrice, suppliers.CompanyName
FROM products
JOIN suppliers ON suppliers.SupplierID = products.SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

-- 3. Create a single query to list the product id, product name, unit price, category name,
--    and supplier name of every product. Order by product name

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName
FROM products AS p
JOIN suppliers AS s ON s.SupplierID = p.SupplierID
JOIN categories AS c ON c.CategoryID = p.CategoryID
ORDER BY ProductName;

-- 4. Create a single query to list the order id, ship name, ship address, and shipping
--    company name of every order that shipped to Germany. Assign the shipping company
--    name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
--    shipped to

SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS Shipper
FROM orders AS o
JOIN shippers AS s
	ON s.ShipperID = o.ShipVia
WHERE o.ShipCountry LIKE 'Germany'
ORDER BY Shipper, ShipName;

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by
--    ship name, with a count of how many orders were shipped for that ship name.

SELECT ShipName, COUNT(OrderID) AS OrdersShipped
FROM orders 
WHERE ShipCountry LIKE 'Germany'
GROUP BY ShipName
ORDER BY ShipName;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all
--    orders that included Sasquatch Ale.

SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders AS o
JOIN `order details` AS od
	ON od.OrderID = o.OrderID
JOIN products AS p
	ON p.ProductID = od.ProductID
WHERE p.ProductName = 'Sasquatch Ale';





