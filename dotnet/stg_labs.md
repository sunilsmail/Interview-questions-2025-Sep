1. temp table vs table variables
2. how to pass table as a param for the Procedure 
3. how to register custom middleware's in c#
4. how to register service in c#
5. how to improve performance of a stored Procedure 

answers for all these questions

Great 👍 These are very common .NET + SQL Server interview questions. I’ll answer each clearly with examples and interview-focused points.

1️⃣ Temp Table vs Table Variable (SQL Server)
🔹 Temporary Table (#TempTable)
CREATE TABLE #Employees (
    Id INT,
    Name VARCHAR(100)
)
✅ Characteristics:

Stored in tempdb

Can create indexes

Supports statistics

Can be used in large data sets

Visible to entire session

Better for complex joins & performance-heavy queries

🔹 Table Variable (@TableVar)
DECLARE @Employees TABLE (
    Id INT,
    Name VARCHAR(100)
)
✅ Characteristics:

Also stored in tempdb (internally)

Limited indexing (only PK/Unique)

No statistics (before SQL 2019)

Scope limited to batch/procedure

Better for small datasets

🔥 Key Differences (Interview Table)
Feature	Temp Table	Table Variable
Stored in	tempdb	tempdb
Statistics	Yes	Limited/No
Index support	Full	Limited
Performance	Better for large data	Better for small data
Scope	Session	Batch/Procedure
Recompile behavior	Can cause recompiles	Less recompiles
🎯 When to use?

✔ Large data → Temp Table

✔ Small data (<100 rows) → Table Variable

✔ Complex joins → Temp Table

2️⃣ How to Pass Table as Parameter to Stored Procedure

You use Table-Valued Parameter (TVP).

Step 1: Create User Defined Table Type
CREATE TYPE EmployeeType AS TABLE
(
    Id INT,
    Name VARCHAR(100)
)
Step 2: Use it in Procedure
CREATE PROCEDURE InsertEmployees
    @Employees EmployeeType READONLY
AS
BEGIN
    INSERT INTO Employees
    SELECT * FROM @Employees
END

⚠ Important:

Must use READONLY

Cannot modify TVP inside procedure

Step 3: Call Procedure
DECLARE @Emp EmployeeType

INSERT INTO @Emp VALUES (1, 'John')

EXEC InsertEmployees @Emp
3️⃣ How to Register Custom Middleware in C#

Assume ASP.NET Core.

Step 1: Create Middleware Class
public class LoggingMiddleware
{
    private readonly RequestDelegate _next;

    public LoggingMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        Console.WriteLine("Request Incoming");

        await _next(context);

        Console.WriteLine("Response Outgoing");
    }
}
Step 2: Register in Program.cs
app.UseMiddleware<LoggingMiddleware>();

OR create extension method:

public static class MiddlewareExtensions
{
    public static IApplicationBuilder UseLogging(
        this IApplicationBuilder builder)
    {
        return builder.UseMiddleware<LoggingMiddleware>();
    }
}

Then:

app.UseLogging();
4️⃣ How to Register Service in C#

Dependency Injection in ASP.NET Core.

🔹 Register Services in Program.cs
builder.Services.AddTransient<IMyService, MyService>();
builder.Services.AddScoped<IMyService, MyService>();
builder.Services.AddSingleton<IMyService, MyService>();
🔥 Difference Between Lifetimes
Lifetime	Meaning
Transient	New instance every time
Scoped	One per HTTP request
Singleton	One for entire app
Inject in Controller
public class HomeController : Controller
{
    private readonly IMyService _service;

    public HomeController(IMyService service)
    {
        _service = service;
    }
}
5️⃣ How to Improve Performance of Stored Procedure

🔥 Very Important Interview Question.

✅ 1. Use Proper Indexes

Clustered index on primary key

Non-clustered on frequently searched columns

✅ 2. Avoid SELECT *

Bad:

SELECT * FROM Employees

Good:

SELECT Id, Name FROM Employees
✅ 3. Avoid Cursors

Use set-based queries instead.

✅ 4. Use EXISTS instead of IN (for large data)

Better:

WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.EmpId = e.Id)
✅ 5. Avoid Functions in WHERE Clause

Bad:

WHERE YEAR(OrderDate) = 2025

Good:

WHERE OrderDate >= '2025-01-01'
AND OrderDate < '2026-01-01'
✅ 6. Use Execution Plan

Check:

Table scan

Index scan

Missing indexes

✅ 7. Parameter Sniffing Fix
OPTION (RECOMPILE)

OR

WITH RECOMPILE
✅ 8. Use Proper Data Types

Avoid NVARCHAR(MAX) unnecessarily

Use INT instead of BIGINT if not needed

✅ 9. Avoid Temp Tables if Not Needed

But use them when breaking complex queries improves performance.

🔥 Quick Interview Summary Answer (If asked verbally)

“For small data I use table variables, for large and complex joins I prefer temp tables.
To pass table as parameter I use Table-Valued Parameters.
Middleware is registered using app.UseMiddleware<T>().
Services are registered using AddTransient, AddScoped, AddSingleton.
Stored procedure performance is improved using indexing, execution plans, avoiding cursors, and fixing parameter sniffing.”
