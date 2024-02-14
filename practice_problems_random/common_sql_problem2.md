this model assumes orders can be from differnet countries. orders belong to a company.

```
Company table:

CompanyID (identifier for the company)
CompanyName (name of the company)
Orders table:

OrderID (identifier for the order)
CompanyID (links the order to the company)
Country (country where the order was made)
OrderAmount (the monetary amount of the order)
```

test data:

```postgresql
CREATE TABLE Company (
    CompanyID SERIAL PRIMARY KEY,
    CompanyName VARCHAR(255)
);

CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    CompanyID INT,
    Country VARCHAR(255),
    OrderAmount DECIMAL(10, 2),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

-- Inserting data into Company
INSERT INTO Company (CompanyName) VALUES
('Global Tech'), ('Innovate Inc.'), ('Eco Solutions'), ('some other company id 4'), ('some other company id 5'), ('some other company id 6');

-- Inserting data into Orders
INSERT INTO Orders (CompanyID, Country, OrderAmount) VALUES
(1, 'USA', 1),
(1, 'Canada', 100), 
(1, 'Canada', 1),
(1, 'Canada', 1),
(1, 'Canada', 1),
(1, 'Canada', 1),
(1, 'Canada', 1),
(1, 'UK', 1),
(1, 'UK', 1),
(1, 'UK', 1),
(1, 'UK', 1),
(2, 'USA', 100),
(2, 'USA', 1),
(2, 'USA', 1),
(2, 'Canada', 1),
(2, 'USA', 1),
(2, 'USA', 1),
(2, 'USA', 1),
(2, 'USA', 1),
(2, 'UK', 1),
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'UK', 1), 
(3, 'USA', 1),
(3, 'USA', 1),
(4, 'USA', 1),
(4, 'USA', 1),
(4, 'USA', 1),
(4, 'UK', 1),
(5, 'UK', 100), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'UK', 1), 
(5, 'USA', 1);
```


sql:
```postgresql
WITH OrderCounts AS (
    SELECT
        Country,
        CompanyID,
        COUNT(OrderID) AS NumberOfOrders,
        RANK() OVER (PARTITION BY Country ORDER BY COUNT(OrderID) DESC) AS Rank
    FROM Orders
    GROUP BY Country, CompanyID
)
SELECT oc.Country, c.CompanyName, oc.NumberOfOrders, Rank
FROM OrderCounts oc
JOIN Company c ON oc.CompanyID = c.CompanyID
WHERE oc.Rank <= 3
ORDER BY oc.Country, oc.Rank;
```

by order amount:

```postgresql
WITH OrderCounts AS (
    SELECT
        Country,
        CompanyID,
        Sum(OrderAmount) AS OrderAmount,
        RANK() OVER (PARTITION BY Country ORDER BY Sum(OrderAmount) DESC) AS Rank
    FROM Orders
    GROUP BY Country, CompanyID
)
SELECT oc.Country, c.CompanyName, oc.OrderAmount, Rank
FROM OrderCounts oc
JOIN Company c ON oc.CompanyID = c.CompanyID
WHERE oc.Rank <= 3
ORDER BY oc.Country, oc.Rank;
```
