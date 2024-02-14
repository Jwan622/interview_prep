Here is some test sql:

```postgresql
CREATE TABLE Company (
    CompanyID SERIAL PRIMARY KEY,
    CompanyName VARCHAR(255),
    Country VARCHAR(255)
);

CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    CompanyID INT,
    OrderAmount DECIMAL(10, 2),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

-- Inserting data into Company
INSERT INTO Company (CompanyName, Country) VALUES
('Tech Innovations', 'USA'),
('Green Solutions', 'USA'),
('companyId_3_usa', 'USA'),
('companyId_4_usa_should_not_appear', 'USA'),
('Data Analytics Inc.', 'Canada'),
('Eco Friendly Co.', 'Canada'),
('Tech Pioneers', 'Canada'),
('company_should_not_appear_canada', 'Canada'),
('Global Tech_should_be_first', 'UK'),
('Renewable Tech', 'UK');

-- Inserting data into Orders
-- companyID 1 has the most orders
-- company 4 has the most order amount
INSERT INTO Orders (CompanyID, OrderAmount) VALUES
(1, 500.00),
(1, 300.00),
(1, 150.00),
(1, 150.00),
(1, 150.00),
(1, 150.00),
(2, 150.00),
(2, 150.00),
(2, 150.00),
(3, 150.00),
(3, 150.00),
(3, 100.00),
(3, 150.00),
(3, 100.00),
(4, 100.00),
(4, 50.00),
(5, 55100.00),
(5, 300.00),
(5, 500.00),
(6, 800.00),
(6, 200.00),
(7, 400.00),
(7, 500.00),
(7, 700.00),
(8, 1.00),
(9, 101.00),
(10, 100.00);
```


sql queries to get top 3 companies by country in order and order amounts:

order counts:
```postgresql
WITH OrderCounts AS (
    SELECT
        c.Country,
        c.CompanyName,
        COUNT(o.OrderID) AS NumberOfOrders,
        RANK() OVER (PARTITION BY c.Country ORDER BY COUNT(o.OrderID) DESC) AS Rank
    FROM Company c
    JOIN Orders o ON c.CompanyID = o.CompanyID
    GROUP BY c.Country, c.CompanyName
)
SELECT Country, CompanyName, NumberOfOrders, Rank
FROM OrderCounts
WHERE Rank <= 3;
```

order amounts
```postgresql
WITH OrderSums AS (
    SELECT
        c.Country,
        c.CompanyName,
        SUM(o.OrderAmount) AS TotalOrderAmount,
        RANK() OVER (PARTITION BY c.Country ORDER BY SUM(o.OrderAmount) DESC) AS Rank
    FROM Company c
    JOIN Orders o ON c.CompanyID = o.CompanyID
    GROUP BY c.Country, c.CompanyName
)
SELECT Country, CompanyName, TotalOrderAmount, Rank
FROM OrderSums
WHERE Rank <= 3;
```
