Here are 20 SQL interview queries every Senior Developer should be comfortable writing and explaining:
#
Question
Key Concept
1
Find the 2nd highest salary
Subquery, DENSE_RANK
2
Find Nth highest salary
Window Functions
3
Find employees earning more than department average salary
GROUP BY, JOIN
4
Find duplicate records
GROUP BY, HAVING
5
Delete duplicate records and keep latest record
ROW_NUMBER
6
Find top 3 salaries in each department
PARTITION BY
7
Find highest salary in each department
DENSE_RANK
8
Running total of salaries
SUM() OVER
9
Find cumulative percentage
Window Functions
10
Find missing IDs in a sequence
Self Join
11
Find employees who never placed an order
LEFT JOIN, NOT EXISTS
12
Find customers with more than one order
GROUP BY
13
Get latest order for each customer
ROW_NUMBER
14
Find consecutive login days
ROW_NUMBER, DATE Logic
15
Find employees hired in last 30 days
Date Functions
16
Pivot rows into columns
PIVOT
17
Unpivot columns into rows
UNPIVOT
18
Find manager and employee hierarchy
Recursive CTE
19
Find department-wise salary ranking
RANK, DENSE_RANK
20
Calculate month-over-month growth
LAG, LEAD
1. Second Highest Salary
SQL
SELECT MAX(Salary)
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);
2. Nth Highest Salary
SQL
WITH CTE AS
(
    SELECT Salary,
           DENSE_RANK() OVER(ORDER BY Salary DESC) RN
    FROM Employees
)
SELECT Salary
FROM CTE
WHERE RN = @N;
3. Salary Greater Than Department Average
SQL
SELECT e.*
FROM Employees e
JOIN
(
    SELECT DeptId,
           AVG(Salary) AvgSalary
    FROM Employees
    GROUP BY DeptId
) d
ON e.DeptId = d.DeptId
WHERE e.Salary > d.AvgSalary;
4. Find Duplicates
SQL
SELECT Email,
       COUNT(*) Cnt
FROM Users
GROUP BY Email
HAVING COUNT(*) > 1;
5. Delete Duplicates
SQL
WITH CTE AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
             PARTITION BY Email
             ORDER BY Id DESC
           ) RN
    FROM Users
)
DELETE
FROM CTE
WHERE RN > 1;
6. Top 3 Salaries Per Department
SQL
WITH CTE AS
(
    SELECT *,
           DENSE_RANK() OVER
           (
             PARTITION BY DeptId
             ORDER BY Salary DESC
           ) RN
    FROM Employees
)
SELECT *
FROM CTE
WHERE RN <= 3;
7. Highest Salary Per Department
SQL
WITH CTE AS
(
    SELECT *,
           DENSE_RANK() OVER
           (
             PARTITION BY DeptId
             ORDER BY Salary DESC
           ) RN
    FROM Employees
)
SELECT *
FROM CTE
WHERE RN = 1;
8. Running Total
SQL
SELECT EmployeeId,
       Salary,
       SUM(Salary) OVER
       (
          ORDER BY EmployeeId
       ) RunningTotal
FROM Employees;
9. Percentage Contribution
SQL
SELECT EmployeeId,
       Salary,
       Salary * 100.0 /
       SUM(Salary) OVER() AS Percentage
FROM Employees;
10. Missing IDs
SQL
SELECT e1.Id + 1 MissingId
FROM Employees e1
LEFT JOIN Employees e2
ON e1.Id + 1 = e2.Id
WHERE e2.Id IS NULL;
11. Customers Without Orders
SQL
SELECT c.*
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerId = o.CustomerId
WHERE o.CustomerId IS NULL;
12. Customers With Multiple Orders
SQL
SELECT CustomerId,
       COUNT(*) OrdersCount
FROM Orders
GROUP BY CustomerId
HAVING COUNT(*) > 1;
13. Latest Order Per Customer
SQL
WITH CTE AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
             PARTITION BY CustomerId
             ORDER BY OrderDate DESC
           ) RN
    FROM Orders
)
SELECT *
FROM CTE
WHERE RN = 1;
14. Consecutive Login Days
SQL
SELECT UserId,
       LoginDate,
       DATEADD(DAY,
               -ROW_NUMBER() OVER
               (
                  PARTITION BY UserId
                  ORDER BY LoginDate
               ),
               LoginDate) grp
FROM UserLogins;
15. Joined Last 30 Days
SQL
SELECT *
FROM Employees
WHERE JoinDate >= DATEADD(DAY,-30,GETDATE());
16. Pivot
SQL
SELECT *
FROM EmployeeSales
PIVOT
(
 SUM(Amount)
 FOR MonthName IN
 (
   Jan,Feb,Mar
 )
) p;
17. Unpivot
SQL
SELECT MonthName,
       Amount
FROM EmployeeSales
UNPIVOT
(
 Amount
 FOR MonthName IN
 (
   Jan,Feb,Mar
 )
) u;
18. Employee Hierarchy
SQL
WITH EmployeeHierarchy AS
(
    SELECT EmployeeId,
           ManagerId,
           Name
    FROM Employees
    WHERE ManagerId IS NULL

    UNION ALL

    SELECT e.EmployeeId,
           e.ManagerId,
           e.Name
    FROM Employees e
    JOIN EmployeeHierarchy h
    ON e.ManagerId = h.EmployeeId
)
SELECT *
FROM EmployeeHierarchy;
19. Department Salary Ranking
SQL
SELECT EmployeeName,
       DeptId,
       Salary,
       RANK() OVER
       (
         PARTITION BY DeptId
         ORDER BY Salary DESC
       ) Ranking
FROM Employees;
20. Month-over-Month Growth
SQL
SELECT Month,
       Revenue,
       LAG(Revenue)
       OVER(ORDER BY Month) PrevRevenue,
       Revenue -
       LAG(Revenue)
       OVER(ORDER BY Month) Growth
FROM RevenueData;
Senior-Level Theory Questions Often Asked Alongside These Queries
Clustered vs Non-Clustered Index
Covering Index
Composite Index
Execution Plan Analysis
Parameter Sniffing
CTE vs Temp Table
EXISTS vs IN
DELETE vs TRUNCATE vs DROP
ACID Properties
Isolation Levels
Deadlocks
Partitioning vs Sharding
Window Functions
Aggregate vs Window Functions
Index Seek vs Index Scan
Statistics in SQL Server
Query Optimization Techniques
Normalization vs Denormalization
Stored Procedure vs Function
NOLOCK and its risks
These are the topics most commonly asked in senior .NET/SQL interviews at banking, fintech, product-based, and enterprise companies.




For a Senior .NET/SQL Developer (8–12 years experience), interviewers usually focus on query writing, performance tuning, indexing, execution plans, CTEs, window functions, and database design.
1. Find the 2nd Highest Salary
SQL
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);
Using DENSE_RANK:
SQL
WITH CTE AS
(
    SELECT Salary,
           DENSE_RANK() OVER(ORDER BY Salary DESC) AS Rnk
    FROM Employees
)
SELECT Salary
FROM CTE
WHERE Rnk = 2;
2. Find Employees Earning More Than Department Average
SQL
SELECT e.*
FROM Employees e
JOIN
(
    SELECT DeptId,
           AVG(Salary) AvgSalary
    FROM Employees
    GROUP BY DeptId
) d
ON e.DeptId = d.DeptId
WHERE e.Salary > d.AvgSalary;
3. Remove Duplicate Records
Keep the latest record.
SQL
WITH CTE AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
               PARTITION BY Email
               ORDER BY Id DESC
           ) RN
    FROM Users
)
DELETE FROM CTE
WHERE RN > 1;
4. Find Nth Highest Salary
SQL
WITH CTE AS
(
    SELECT Salary,
           DENSE_RANK() OVER(ORDER BY Salary DESC) RN
    FROM Employees
)
SELECT Salary
FROM CTE
WHERE RN = @N;
5. Find Duplicate Records
SQL
SELECT Email,
       COUNT(*) CountOfRecords
FROM Users
GROUP BY Email
HAVING COUNT(*) > 1;
6. Running Total
SQL
SELECT EmployeeId,
       Salary,
       SUM(Salary) OVER
       (
           ORDER BY EmployeeId
       ) RunningTotal
FROM Employees;
7. Top 3 Salaries Per Department
SQL
WITH CTE AS
(
    SELECT *,
           DENSE_RANK() OVER
           (
               PARTITION BY DeptId
               ORDER BY Salary DESC
           ) RN
    FROM Employees
)
SELECT *
FROM CTE
WHERE RN <= 3;
8. Find Missing IDs
IDs: 1,2,3,5,6,8
Output: 4,7
SQL
SELECT t1.Id + 1 AS MissingId
FROM Employee t1
LEFT JOIN Employee t2
ON t1.Id + 1 = t2.Id
WHERE t2.Id IS NULL;
9. Find Employees Joined in Last 30 Days
SQL
SELECT *
FROM Employees
WHERE JoinDate >= DATEADD(DAY,-30,GETDATE());
10. Pivot Data
SQL
SELECT *
FROM
(
    SELECT DeptName, EmployeeName
    FROM Employees
) src
PIVOT
(
    COUNT(EmployeeName)
    FOR DeptName IN
    (
        HR,
        IT,
        Finance
    )
) p;
11. Get Latest Record Per Customer
SQL
WITH CTE AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
               PARTITION BY CustomerId
               ORDER BY CreatedDate DESC
           ) RN
    FROM Orders
)
SELECT *
FROM CTE
WHERE RN = 1;
12. Consecutive Login Days
SQL
WITH CTE AS
(
    SELECT UserId,
           LoginDate,
           ROW_NUMBER() OVER
           (
               PARTITION BY UserId
               ORDER BY LoginDate
           ) RN
    FROM UserLogins
)
SELECT *
FROM CTE;
(Interviewers often ask how to find 3+ consecutive days using this pattern.)
13. Difference Between ROW_NUMBER, RANK and DENSE_RANK
Example salaries:
Salary
ROW_NUMBER
RANK
DENSE_RANK
10000
1
1
1
9000
2
2
2
9000
3
2
2
8000
4
4
3
14. CTE vs Temp Table
CTE
Temporary result set
Exists only for query execution
Good for recursive queries
Temp Table
Stored in tempdb
Can be indexed
Better for large datasets
15. Aggregate vs Window Functions
Aggregate:
SQL
SELECT DeptId,
       AVG(Salary)
FROM Employees
GROUP BY DeptId;
Window:
SQL
SELECT EmployeeName,
       Salary,
       AVG(Salary) OVER(PARTITION BY DeptId)
FROM Employees;
Aggregate reduces rows; window functions retain rows.
Performance Tuning Questions (Very Common)
Why is query slow?
Check:
Missing indexes
Table scans
Parameter sniffing
Outdated statistics
Large joins
Scalar functions in WHERE clause
Clustered vs Non-Clustered Index
Clustered
Actual data stored in sorted order
One per table
Non-Clustered
Separate structure containing key + pointer
Multiple per table
EXISTS vs IN
Prefer EXISTS for large datasets.
SQL
SELECT *
FROM Employees e
WHERE EXISTS
(
    SELECT 1
    FROM Departments d
    WHERE d.Id = e.DeptId
);
Interview Favorite Query
Find the employee with the highest salary in each department.
SQL
WITH CTE AS
(
    SELECT *,
           DENSE_RANK() OVER
           (
               PARTITION BY DeptId
               ORDER BY Salary DESC
           ) RN
    FROM Employees
)
SELECT *
FROM CTE
WHERE RN = 1;
These are among the most frequently asked senior-level SQL questions in product companies, banking projects, and enterprise .NET interviews.