Q. Find the top performing merchants for each day.
Q. Write a query to find the total number of customers and the first time customers who ordered with the top-performing merchant that day. First time customers are the customers who ordered never before that delivery date.
Q. Find top performing merchants for each day with the Total_Amount_Earned on the previous day.


Entities and Attributes
Customers

CustomerID (Primary Key)
Name
Email
RegistrationDate
LastOrderDate (to quickly filter first-time customers)
Merchants

MerchantID (Primary Key)
MerchantName
RegistrationDate
Category (e.g., food, groceries)
Deliveries

DeliveryID (Primary Key)
CustomerID (Foreign Key)
MerchantID (Foreign Key)
DeliveryDate
TotalAmount
DeliveryStatus
MerchantEarnings

EarningsID (Primary Key)
MerchantID (Foreign Key)
Date
TotalAmountEarned

Relationships
Customers to Deliveries: One-to-Many (a customer can have multiple deliveries)
Merchants to Deliveries: One-to-Many (a merchant can have multiple deliveries)
Merchants to MerchantEarnings: One-to-Many (earnings recorded per day)


## SQL Queries

### Top Performing Merchants Each Day
SELECT MerchantID, SUM(TotalAmount) as TotalEarnings, DeliveryDate   
FROM Deliveries 
GROUP BY MerchantID, DeliveryDate 
ORDER BY TotalEarnings DESC;   # you can use TotalEarnings in the ORDER BY



### Total Number of Customers and First-Time Customers for Top Merchant
WITH TopMerchant AS ( ## Do this first
    SELECT MerchantID, DeliveryDate 
    FROM Deliveries 
    GROUP BY MerchantID, DeliveryDate 
    ORDER BY SUM(TotalAmount) DESC 
    LIMIT 1
)
SELECT COUNT(DISTINCT CustomerID) AS TotalCustomers, 
       COUNT(DISTINCT CASE WHEN LastOrderDate IS NULL THEN CustomerID END) AS FirstTimeCustomers  # can use CASE in the COUNT
FROM Deliveries 
JOIN TopMerchant ON Deliveries.MerchantID = TopMerchant.MerchantID 
AND Deliveries.DeliveryDate = TopMerchant.DeliveryDate;
Top Performing Merchants with Previous Day's Earnings

### Top Performing Merchants with Previous Day's Earnings
SELECT D.MerchantID, D.DeliveryDate, ME.TotalAmountEarned AS PreviousDayEarnings
FROM Deliveries D
JOIN MerchantEarnings ME ON D.MerchantID = ME.MerchantID 
AND ME.Date = DATE_SUB(D.DeliveryDate, INTERVAL 1 DAY)
GROUP BY D.MerchantID, D.DeliveryDate
ORDER BY SUM(D.TotalAmount) DESC;

### Additional Considerations
Indexes: Indexing fields like MerchantID and CustomerID in Deliveries can speed up queries.
Data Consistency: Ensure foreign key constraints for data integrity.
Performance: For large datasets, consider optimizing queries and the database structure.
