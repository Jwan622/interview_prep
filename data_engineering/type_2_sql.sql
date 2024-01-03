--This is an example of a Type II slowly changing dimension table that keeps track of changes to a user’s profile.
-- We use LAG() to determine the previous value
-- We use LEAD() to leave the current updates unexpired
-- We use the current row in the database as a starting point so that incoming rows aren’t all interpreted as ‘adds’
-- It’s all pure SQL. On a high level, we compare incoming rows in a staging table to current rows and calculate the diff.

create schema if not exists jeff_test;


drop table if exists jeff_test.users;
CREATE TABLE jeff_test.users (
   id serial PRIMARY KEY,
   first_name VARCHAR ( 32 ) NOT NULL,
   last_name VARCHAR ( 32 ) NOT NULL,
   email VARCHAR ( 256 ) UNIQUE NOT NULL,
   zodiac_sign VARCHAR (64),
   created_on TIMESTAMP NOT NULL,
   updated_at TIMESTAMP NOT NULL
);


INSERT INTO jeff_test.users(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (1, 'jeff', 'wan', 'jwan0622@yahoo.com', 'virgo', '2022-01-01T00:01:34Z', '2022-01-01T00:01:01Z');
INSERT INTO jeff_test.users(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (2, 'spencer', 'kwon', 'skwon0622@yahoo.com', 'cancer', '2022-01-02T00:01:34Z', '2022-01-02T00:01:01Z');
INSERT INTO jeff_test.users(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (3, 'viv', 'chang', 'vchang0622@yahoo.com', 'pisces', '2022-01-03T00:01:34Z', '2022-01-03T00:01:01Z');


drop table if exists jeff_test.users_staging;
CREATE TABLE jeff_test.users_staging (
   id integer NOT NULL,
   first_name VARCHAR ( 32 ) NOT NULL,
   last_name VARCHAR ( 32 ) NOT NULL,
   email VARCHAR ( 256 ) NOT NULL,
   zodiac_sign VARCHAR (64),
   created_on TIMESTAMP NOT NULL,
   updated_at TIMESTAMP NOT NULL
);


INSERT INTO jeff_test.users_staging(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (1, 'jeff', 'wan', 'jwan0622@yahoo.com', 'cancer', '2022-01-01T00:01:34Z', '2024-01-01T00:01:01Z');  -- this should be an update of zodiac to cancer so curr_value will = cancer
INSERT INTO jeff_test.users_staging(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (2, 'spencer', 'kwon', 'skwon0622@yahoo.com', 'virgo', '2022-01-02T00:01:34Z', '2024-01-02T00:01:01Z'); -- this should be an update of zodiac to virgo so curr_value will = virgo
INSERT INTO jeff_test.users_staging(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (3, 'viv', 'chang', 'vchang06221@yahoo.com', 'pisces', '2022-01-03T00:01:34Z', '2024-01-03T00:01:01Z'); -- this should be an update of zodiac to pisces so curr_value will = pisces
INSERT INTO jeff_test.users_staging(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (4, 'new', 'person', 'new_person@yahoo.com', 'gemini', '2024-01-03T00:01:34Z', '2024-01-04T00:01:01Z'); -- this is a new user so every row should be an add.
INSERT INTO jeff_test.users_staging(id, first_name, last_name, email, zodiac_sign, created_on, updated_at) VALUES (4, 'new', 'person', 'new_person@yahoo.com', 'cancer', '2024-01-03T00:01:34Z', '2024-01-05T00:01:01Z'); -- this should expire the gemini row for this last user


drop table if exists jeff_test.users_audit;
CREATE TABLE jeff_test.users_audit (
   users_audit_oid VARCHAR(128),
   id bigint NOT NULL,
   column_name VARCHAR ( 32 ) NOT NULL,
   audit_action VARCHAR ( 32 ) NOT NULL,
   curr_value VARCHAR ( 256 ) NOT NULL,
   prev_value VARCHAR ( 256 ),
   effective_from TIMESTAMP NOT NULL,
   expired_on TIMESTAMP
);




WITH incoming_users AS (
   -- we need the 0 because later on we don't want to create audits for rows that are already in the database but we need the current row to determine the diff in values otherwise very incoming row will be an 'add'
   SELECT *, 0 as is_current FROM jeff_test.users_staging
), current_users AS (
   SELECT *, 1 as is_current FROM jeff_test.users
   WHERE id IN (SELECT id FROM incoming_users)
), current_and_incoming AS (
   select * from current_users
            UNION ALL
   select * from incoming_users
), prev_and_curr_values as (
   -- this gets the previous values for each incoming row
   select  *,
           LAG(first_name) OVER (PARTITION BY id ORDER BY updated_at, created_on ASC) as prev_first_name,
           LAG(last_name) OVER (PARTITION BY id ORDER BY updated_at, created_on ASC) as prev_last_name,
           LAG(email) OVER (PARTITION BY id ORDER BY updated_at, created_on ASC) as prev_email,
           LAG(zodiac_sign) OVER (PARTITION BY id ORDER BY updated_at, created_on ASC) as prev_zodiac_sign
   from current_and_incoming
), all_changes as (
   SELECT
       id AS id,
       'first_name' AS column_name,
       first_name AS curr_value,
       prev_first_name AS prev_value,
       updated_at AS effective_from,
       created_on AS created_on
   FROM prev_and_curr_values
   WHERE prev_first_name <> first_name OR prev_first_name IS NULL
   AND is_current = 0


   UNION ALL


   SELECT
       id AS id,
       'last_name' AS column_name,
       last_name AS curr_value,
       prev_last_name AS prev_value,
       updated_at AS effective_from,
       created_on AS created_on
   FROM prev_and_curr_values
   WHERE prev_last_name <> last_name OR prev_last_name IS NULL
   AND is_current = 0


   UNION ALL


   SELECT
       id AS id,
       'email' AS column_name,
       email AS curr_value,
       prev_email AS prev_value,
       updated_at AS effective_from,
       created_on AS created_on
   FROM prev_and_curr_values
   WHERE prev_email <> email OR prev_email IS NULL
   AND is_current = 0


   UNION ALL


   SELECT
       id AS id,
       'zodiac_sign' AS column_name,
       zodiac_sign AS curr_value,
       prev_zodiac_sign AS prev_value,
       updated_at AS effective_from,
       created_on AS created_on
   FROM prev_and_curr_values
   WHERE prev_zodiac_sign <> zodiac_sign OR prev_zodiac_sign IS NULL
   AND is_current = 0
) -- select * from all_changes


-- we're not doing this yet, but we can grab the rows we're about to insert, LEFT JOIN to the audit on the oid, and only add rows that are not found in the audit table
INSERT INTO jeff_test.users_audit (users_audit_oid, id, column_name, audit_action, curr_value, prev_value, effective_from, expired_on)
SELECT
   md5(cast(id as text) || column_name || curr_value) as users_audit_oid, -- this is to ensure during reruns of this procedure, we don't audit duplicates, we can use this to only insert rows that don't already exist in the audit table
   id,
   column_name,
   CASE
       WHEN prev_value IS NULL THEN 'add'
       ELSE 'update'
       END AS audit_action,
   curr_value,
   prev_value,
   effective_from,
   NULL as expired_on
FROM all_changes;


-- this expires the old zodiac add audit which is accurate. all the present updates should be unexpired.
update jeff_test.users_audit
   set expired_on = tt.expired_date
   from (select id, column_name, lead(effective_from) over (PARTITION BY id, column_name order by effective_from ASC) as expired_date
         from jeff_test.users_audit
        ) as tt
   where tt.id = jeff_test.users_audit.id and tt.column_name = jeff_test.users_audit.column_name and expired_date <> jeff_test.users_audit.effective_from;


select * from jeff_test.users_audit;

