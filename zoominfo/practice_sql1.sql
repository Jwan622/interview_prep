-- get the timestamps for the user's first and last activity and the associated activity type

CREATE TABLE activities (
    userid INTEGER,
    activity_timestamp TIMESTAMP,
    activity_type CHAR(1)
);

INSERT INTO activities (userid, activity_timestamp, activity_type) VALUES
(1, '2022-01-01 08:00:00', 'A'),
(1, '2022-01-01 09:00:00', 'B'),
(1, '2022-01-01 09:00:00', 'Y'),
(2, '2022-01-02 10:00:00', 'A'),
(2, '2022-01-02 11:00:00', 'C'),
(3, '2022-01-03 12:00:00', 'B'),
(3, '2022-01-03 13:00:00', 'A'),
(4, '2022-01-04 14:00:00', 'C'),
(4, '2022-01-04 15:00:00', 'B'),
(5, '2022-01-05 16:00:00', 'A'),
(5, '2022-01-05 17:00:00', 'C'),
(6, '2022-01-06 18:00:00', 'B'),
(6, '2022-01-06 19:00:00', 'A'),
(7, '2022-01-07 20:00:00', 'C'),
(7, '2022-01-07 21:00:00', 'B'),
(7, '2022-01-07 22:00:00', 'A'),
(7, '2022-01-07 23:00:00', 'Z'),
(8, '2022-01-01 00:00:00', 'B');

select * from activities;


-- best I think is ranked and joining
WITH ranked AS (
    SELECT
        userid,
        activity_timestamp,
        activity_type,
        ROW_NUMBER() OVER(PARTITION BY userid ORDER BY activity_timestamp ASC) AS ranked_asc,
        ROW_NUMBER() OVER(PARTITION BY userid ORDER BY activity_timestamp DESC) AS ranked_desc
    FROM
        activities
) select COALESCE(fa.userid, la.userid),
        fa.activity_timestamp as first_act_timestamp,
        fa.activity_type as first_act_type,
        la.activity_timestamp as last_act_timestamp,
        la.activity_type as last_act_type,
        fa.ranked_asc,
        la.ranked_desc
  FROM ranked as fa
  INNER JOIN ranked as la
  ON fa.userid = la.userid
  AND fa.ranked_asc = 1 and la.ranked_desc = 1;


-- hard to reason about with group by
-- WITH ranked AS (
--     SELECT
--         userid,
--         activity_timestamp,
--         activity_type,
--         ROW_NUMBER() OVER(PARTITION BY userid ORDER BY activity_timestamp ASC) AS ranked_asc,
--         ROW_NUMBER() OVER(PARTITION BY userid ORDER BY activity_timestamp DESC) AS ranked_desc
--     FROM
--         activities
-- ) select userid,
--         MAX(CASE WHEN ranked_asc = 1 then activity_type END) as first_activity_type,
--         MAX(CASE WHEN ranked_desc = 1 then activity_type END) as last_activity_type,
--         MAX(case when ranked_asc = 1 then activity_timestamp end) as first_timestamp,
--         MAX(case when ranked_desc = 1 then activity_timestamp end) as last_timestamp
--   from ranked
--   group by userid;



-- alternative
with first_activity as (
    select *,
        row_number() over (PARTITION BY userid order by activity_timestamp ASC) as ranked_earliest
    from activities
), last_activity as (
    select *,
        row_number() over (PARTITION BY userid order by activity_timestamp DESC) as ranked_latest
    from activities
)
select fa.userid,
        fa.activity_timestamp as first_activity_timestamp,
        fa.activity_type as first_activity_type,
        la.activity_timestamp as last_activity_timestamp,
        la.activity_type as last_activity_type
FROM first_activity AS fa
INNER JOIN last_activity as la
ON la.userid = fa.userid
AND la.ranked_latest = 1 AND fa.ranked_earliest = 1;
