https://leetcode.com/problems/department-highest-salary/

Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.


Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.


Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.


# Write your MySQL query statement below
# select Department, Employee, Salary FROM
# (
#   select d.name as Department,
#   e.name as Employee,
#   e.salary as Salary,
#   dense_rank() over ( partition by d.name order by e.salary desc ) as r
# FROM Employee as e
# INNER JOIN Department as d
# ON d.id = e.departmentId) as t
# where r = 1

WITH DepartmentMaxSalary AS (
  SELECT
    e.departmentId AS departmentId,
    MAX(e.salary) AS maxSalary
  FROM Employee e #so this just gets the max salary in each apartment. if there's a tie, we don't know anything else like which employees have that max salary. This table is just salary and department Id
  GROUP BY e.departmentId
)

SELECT
  d.name AS Department,
  e.name AS Employee,
  e.salary AS Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id # get all the employee and department names
INNER JOIN DepartmentMaxSalary ms ON e.departmentId = ms.departmentId and e.salary = ms.maxSalary # this will get all the employees with that max salary
