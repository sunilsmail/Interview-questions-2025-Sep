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