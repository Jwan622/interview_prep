imagine three tables, orders and merchants and dashers
    
orders has these columns:
subtotal (gross income)
total
dasher_id
order_id
merchant_id
is_pickup (0 or 1, 0 means deliver, 1 is pickup)
status (cancelled or completed)

merchants table:
id
name

dashers table:
id
name


questions I was asked:
1. dashers who did not deliver to the top 5 merchants by subtotal
2. cancelled deliveries total as a percentage of deliveries total
3. top 3 merchants by order total with more than 1 order

1.  
with top_5_merchants_by_total as (
    SELECT merchant_id,
        SUM(total) as total
        FROM orders
        GROUP by merchant_id
        ORDER BY SUM(total) desc
        LIMIT 5
), dashers_who_have_delivered_to_top_5 as (
    select distinct dasher_id from orders where merchant_id IN (select merchant_id from top_5_merchants_by_total
)
SELECT d.id AS DasherID, 
    d.name AS DasherName
FROM dashers d
WHERE d.id NOT IN ( # this subquery is needed. get dasher ids who are not delivered to top 5 ever 
    SELECT dasher_id from dashers_who_have_delivered_to_top_5
) # all dashers - dashers who have delivered to top 5 merchants = dashers who have never delivered to top 5

2. 
SELECT
    SUM(CASE WHEN o.status = 'cancelled' THEN 1 ELSE 0 END) AS CancelledDeliveries,
    COUNT(*) AS TotalDeliveries,
    CancelledDeliveries/TotalDeliveries * 100 AS PercentageCancelled
FROM orders o
WHERE o.is_pickup = 0;  -- Consider only deliveries, not pickups

3. 
SELECT o.merchant_id
    SUM(o.total) AS TotalOrderAmount
FROM orders o
INNER JOIN merchants m 
ON o.merchant_id = m.id
GROUP BY o.merchant_id
HAVING count(o.id) > 1
ORDER BY TotalOrderAmount DESC
LIMIT 3;


