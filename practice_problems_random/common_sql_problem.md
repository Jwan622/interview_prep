Here is some test sql:
this model assumes orders belong to a company but a company is from one country. So orders aren't from different countries.

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


jsut run that to see. Also see how this works too to explain why you need the double GROUP BY and why you're partitioning by `Country`.


the below highlights that you need the group by both to get the order amount or order count on a per country and per company basis. And then you can rank it and partition by country to get the top 3 per country by order count/amount per country.
```
SELECT
        c.CompanyName,
        SUM(o.OrderAmount) AS TotalOrderAmount,
        RANK() OVER (PARTITION BY c.CompanyName ORDER BY SUM(o.OrderAmount) DESC) AS Rank
    FROM Company c
    JOIN Orders o ON c.CompanyID = o.CompanyID
    GROUP BY c.CompanyName
;
            companyname            | totalorderamount | rank
-----------------------------------+------------------+------
 Data Anaulytics Inc.               |         55900.00 |    1
 Eco Friendly Co.                  |          1000.00 |    1
 Global Tech_should_be_first       |           101.00 |    1
 Green Solutions                   |           450.00 |    1
 Renewable Tech                    |           100.00 |    1
 Tech Innovations                  |          1400.00 |    1
 Tech Pioneers                     |          1600.00 |    1
 companyId_3_usa                   |           650.00 |    1
 companyId_4_usa_should_not_appear |           150.00 |    1
 company_should_not_appear_canada  |             1.00 |    1
(10 rows)
```
