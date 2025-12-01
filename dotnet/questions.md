

AI Mode
All
Images
Videos
News
Maps
Shopping
Books
Flights
Finance

undefined
2 sites
Here are the answers to the .NET interview questions listed in the image, with examples.
WEB API
What is REST, and how is it implemented in ASP.NET Web API?
REST (Representational State Transfer) is an architectural style for networked applications based on standard HTTP verbs (GET, POST, PUT, DELETE) and resource-based URLs.
In ASP.NET Web API, it's implemented using ApiController classes. The framework automatically maps HTTP requests to methods (actions) within the controller using conventions and routing attributes like [HttpGet], [HttpPost], etc.
Example: A GET /api/products request would map to a GetProducts() method decorated with [HttpGet] in the ProductsController.
How do you secure a Web API (JWT, OAuth, API keys, etc.)?
Web APIs are typically secured using:
JWT (JSON Web Tokens): After a user logs in, the server issues a token that the client includes in subsequent requests for authentication and authorization.
OAuth 2.0: An authorization framework that allows third-party applications to obtain limited access to a web service.
API Keys: A simple method where a unique key is sent with each request, often in a header or query parameter, to identify the client application.
Difference between IActionResult and ActionResult in .NET Core?
IActionResult is an interface that allows an action method to return any type of response, such as a view, status code, or JSON data. It requires manual casting and type checks in the client code.
ActionResult<T> is a wrapper class introduced in .NET Core 2.1 that allows you to return a specific type T (e.g., a list of products) or any standard IActionResult (e.g., NotFound()). This provides better type safety and documentation.
Example (ActionResult<T>):
csharp
[HttpGet("{id}")]
public ActionResult<Product> GetProduct(int id)
{
    var product = _context.Products.Find(id);
    if (product == null)
    {
        return NotFound();
    }
    return product; // Automatically wraps the product in Ok(product)
}
Use code with caution.

How do you implement versioning in Web API?
Versioning allows you to support multiple versions of your API simultaneously. Common approaches include:
URI Path: Including the version in the URL (e.g., /api/v1/products).
Query String: Using a query parameter (e.g., /api/products?api-version=1.0).
Custom Request Headers: Specifying the version in a custom HTTP header.
Media Types (Content Negotiation): Using a custom media type in the Accept header.
What's the difference between middleware and filters in ASP.NET Core?
Middleware forms a pipeline that handles every HTTP request and response. It can modify the request, short-circuit the pipeline, or perform cross-cutting concerns like logging, authentication, and exception handling.
Filters are used within the MVC or Web API pipeline to inject logic at specific stages of action execution, such as authorization ([Authorize]), action execution ([HttpGet]), or result execution. They have access to the context of the action method being called.
ENTITY FRAMEWORK (EF)
Difference between code-first, database-first, and model-first approaches?
Code-First: You write the C# classes (models) first, and EF Core generates the database schema based on those classes and configurations. This is the most popular approach in modern development.
Database-First: You start with an existing database, and EF Core tools generate the C# entity classes and DbContext automatically.
Model-First: You design a visual model (.edmx file) of your entities and relationships in a designer, and EF generates both the C# classes and the database script from the model. This approach is largely deprecated in EF Core.
Explain eager loading vs lazy loading vs explicit loading.
These are methods for loading related data (e.g., loading an Author with their Books).
Eager Loading: Related data is loaded from the database as part of the initial query using the .Include() or .ThenInclude() methods.
Example: var blogs = context.Blogs.Include(b => b.Posts).ToList();
Lazy Loading: Related data is loaded automatically the first time you access the navigation property, requiring extra database round trips. This usually requires proxy classes or configuration.
Explicit Loading: You manually load the related data at a later point in time using the Load() method on the entity's entry reference or collection.
What's the difference between DbContext and ObjectContext?
ObjectContext was the primary class in older versions of Entity Framework (EF6 and earlier). DbContext is a lightweight wrapper around ObjectContext and is the main class used in EF Core and most modern EF applications. DbContext has a simpler and cleaner API.
How do you handle transactions in EF Core?
EF Core automatically wraps standard operations like SaveChanges() in a transaction by default. For more control over multiple operations or explicit transactions, you use the Database.BeginTransaction(), CommitTransaction(), and RollbackTransaction() methods.
Example:
csharp
using (var transaction = context.Database.BeginTransaction())
{
    try
    {
        context.Users.Add(user1);
        context.SaveChanges();
        context.Users.Add(user2);
        context.SaveChanges();
        transaction.Commit();
    }
    catch
    {
        transaction.Rollback();
    }
}
Use code with caution.

What are migrations in EF Core and how do you use them?
Migrations are a way to incrementally update the database schema to match changes in your entity data model over time.
You use the Add-Migration <Name> command in the Package Manager Console to scaffold migration classes and the Update-Database command to apply the changes to the database.
LINQ
Difference between IEnumerable, IQueryable, and List?
List<T> is a concrete collection that holds items in memory.
IEnumerable is an interface for iterating over a collection. It supports deferred execution (using yield return) but processes filtering on the client side (in memory) if a data source is involved.
IQueryable inherits from IEnumerable. It represents a query that is executed on the server side (e.g., in the SQL database). It translates LINQ queries into database-specific commands (like SQL queries), which is more efficient for large datasets.
Explain deferred execution vs immediate execution in LINQ.
Deferred Execution means the LINQ query is not executed immediately when it is defined. The execution is delayed until you actually iterate over the results (e.g., using a foreach loop or methods like .ToList(), .ToArray()). Most LINQ operators support this.
Immediate Execution happens when you use methods that force the query to run right away, such as .ToList(), .Count(), .Average(), or .First().
How do joins work in LINQ (inner, left, group joins)?
LINQ supports standard join operations through query syntax or extension methods:
Inner Join: Returns only elements that have matching keys in both sequences.
Left Outer Join: Returns all elements from the first sequence and only matching elements from the second.
Group Join: Groups results from the second sequence based on a match with the first, effectively creating a hierarchical result.
How can you optimize LINQ queries for performance?
Optimization techniques include:
Using IQueryable when querying remote data sources to push logic to the server.
Selecting only necessary columns using .Select() to minimize data transfer.
Avoiding calling methods like .ToList() inside loops (forces immediate execution).
Using asynchronous methods (async/await) for I/O operations.
Example of using SelectMany and when it's useful.
SelectMany is used to project elements of a sequence into a single flat sequence by combining the results of a collection selector function. It's useful for flattening nested collections.
Example: Flattening a list of students from multiple classes into a single list of all students.
csharp
List<Class> classes = GetClassesWithStudents();
IEnumerable<Student> allStudents = classes.SelectMany(c => c.Students);
Use code with caution.

.NET CORE
What are the main differences between .NET Framework and .NET (Core)?
.NET Framework is Windows-only and primarily used for Windows Forms/WPF and classic ASP.NET applications.
.NET (Core) is cross-platform (Windows, macOS, Linux), open-source, modular, and optimized for performance, cloud-native apps, and microservices. It is the modern, recommended version of .NET.
Explain dependency injection in .NET Core.
Dependency Injection (DI) is a design pattern used to achieve Inversion of Control (IoC) between classes and their dependencies. .NET Core has built-in support for DI. Services are registered in the Startup.cs (or Program.cs) file and are provided to classes via their constructors, making the code loosely coupled and easier to test.
What is the role of IHostedService in .NET Core?
IHostedService is an interface used to run background tasks or long-running operations in a non-blocking way within an ASP.NET Core application (or any generic host). It provides StartAsync() and StopAsync() methods to manage the lifetime of the background service with the host's lifetime.
What is Kestrel and how does it work in ASP.NET Core?
Kestrel is an open-source, cross-platform web server that is included by default in all ASP.NET Core projects. It is fast, lightweight, and handles HTTP requests directly. In many production scenarios, Kestrel is run behind a more robust server like IIS, Nginx, or Apache, which acts as a reverse proxy.
How do you manage configuration in .NET Core (appsettings.json, environment variables, etc.)?
.NET Core uses a flexible configuration system that allows settings to be loaded from various sources. The default hierarchy typically includes appsettings.json, environment variables, user secrets, and command-line arguments. Later sources override earlier ones.
What are minimal APIs introduced in .NET 6?
Minimal APIs allow developers to build HTTP APIs with minimal dependencies and lines of code. They simplify the setup process by allowing you to define routes and actions using a simple lambda expression syntax directly in the Program.cs file, without the need for controllers or complex setup.
How does middleware pipeline work in .NET Core?
The middleware pipeline is a sequence of components assembled in the Configure method (or directly in Program.cs using app.Use... methods) that handle HTTP requests. Each component can decide whether to pass the request to the next component in the sequence or to short-circuit the pipeline and return a response directly.
What is the difference between transient, scoped, and singleton lifetimes?
These define how long a service instance lives within the DI container:
Transient: A new instance of the service is created every time it is requested.
Scoped: A single instance is created once per client request (connection) and is reused throughout the lifetime of that request.
Singleton: A single instance is created the first time it is requested and is reused by all subsequent requests throughout the application's lifetime.
How do you handle logging in .NET Core?
.NET Core uses the ILogger and ILoggerProvider interfaces for a unified logging system. It supports various built-in and third-party logging providers (Console, Debug, Event Source, Azure App Services, NLog, Serilog, etc.). You inject ILogger<T> into your classes and use methods like LogInformation(), LogError(), etc.
Are you interested in a deeper dive into any specific question or an example in C# code?
AI can make mistakes, so double-check responses



Top 15 .NET Interview Questions for 3+ Years of Experience (With ...

Medium

If You Can Answer These Additional 7 Questions Correctly, You're ...

Medium

Ask anything


All items removed from input context.AI Mode response is ready