I think this was one of the questions they asked me during the interview. It was something aobut hotel bookings in cities.

The schema was something as follows:

CREATE TABLE hotels (
    id          varchar(16),
    name        varchar(40),
    country     varchar(40),
    city        varchar(40),
    start_date  date
);

CREATE TABLE users (
    id                  varchar(16),
    name                varchar(40),
    registration_date   date
);


CREATE TABLE bookings (
    id          varchar(16),
    name        varchar(40),
    amount      varchar(40),
    users_id    varchar(16),
    hotel_id    varchar(16)
    date        date
);

1. find most popular hotel in each city.
- Window Function Needed for Each City: To find the most popular hotel in each city, you need a window function to rank hotels within each city.

SELECT 
    city, 
    hotel_name, 
    booking_count
FROM (
    SELECT 
        h.city, 
        h.name AS hotel_name, 
        COUNT(b.id) AS booking_count,
        RANK() OVER (PARTITION BY h.city ORDER BY COUNT(b.id) DESC) AS rnk
    FROM 
        bookings b
    INNER JOIN 
        hotels h ON h.id = b.hotel_id
    GROUP BY 
        h.city, h.name
) AS ranked_hotels
WHERE rnk = 1;

This query uses a window function (RANK()) to rank the hotels by booking count within each city and then selects only the top-ranked hotel in each city.

2. For users who registered in the last 30 days, find which user had the most bookings.

first identify users who registered in 30 days in one cte, then find their bookings and who had the most

with recent_30d_users as (
    select * from users where registration_date > current_date - interval '30' day;
)
SELECT 
    u.id AS user_id,
    u.name AS user_name,
    COUNT(b.id) AS booking_count
FROM 
    recent_30d_users u
LEFT JOIN 
    bookings b ON u.id = b.users_id
GROUP BY 
    u.id
ORDER BY 
    COUNT(b.id) DESC
LIMIT 1;



Using a Common Table Expression (CTE) as we did is a valid and organized way to approach this. Your query effectively separates the process into two parts: first identifying recent users and then calculating their booking counts. Here's how your query works:

CTE (Common Table Expression): You've created a CTE named recent_30d_users, which selects all users who registered in the last 30 days. This is a neat way to isolate this part of the logic.

Main Query:

FROM recent_30d_users u: You then use the CTE in the main query, joining it with the bookings table.

LEFT JOIN bookings b ON u.id = b.users_id: This joins the recent users with their bookings. A left join ensures that you include all recent users, even if they haven't made any bookings.

SELECT and GROUP BY: The main SELECT statement retrieves the user ID, user name, and the count of bookings they have made. The GROUP BY clause groups this information by user.

ORDER BY and LIMIT: Finally, the results are ordered by the booking count in descending order, and LIMIT 1 is used to get the user with the most bookings.



3. Which was the most popular booked hotel in the last 2 months?




