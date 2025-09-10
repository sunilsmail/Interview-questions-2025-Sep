1. Move all duplicates to the end of an array
<details> <summary>👉 Answer</summary>

Logic: Use a set to track seen elements, maintain order for unique elements, and push duplicates at the end.

JavaScript Example:
```js
function moveDuplicates(arr) {
  let seen = new Set();
  let uniques = [];
  let duplicates = [];

  for (let item of arr) {
    if (seen.has(item)) {
      duplicates.push(item);
    } else {
      seen.add(item);
      uniques.push(item);
    }
  }
  return [...uniques, ...duplicates];
}

console.log(moveDuplicates([1, 2, 3, 2, 4, 3, 5]));
// Output: [1, 2, 3, 4, 5, 2, 3]
```
```python
Python Example:

def move_duplicates(arr):
    seen = set()
    unique, dupes = [], []
    for num in arr:
        if num in seen:
            dupes.append(num)
        else:
            seen.add(num)
            unique.append(num)
    return unique + dupes

print(move_duplicates([1,2,3,2,4,3,5]))
# Output: [1,2,3,4,5,2,3]
```
</details>
2. Insert records in chunks
<details> <summary>👉 Answer</summary>

Problem: DB supports only limited inserts per batch.
Solution: Process in chunks.

C# Example:
```cs
public void SaveInChunks(List<int> records, int chunkSize)
{
    for (int i = 0; i < records.Count; i += chunkSize)
    {
        var batch = records.Skip(i).Take(chunkSize).ToList();
        SaveToDB(batch);
    }
}
```

JavaScript Example:
```js
function saveInChunks(records, chunkSize) {
  for (let i = 0; i < records.length; i += chunkSize) {
    const batch = records.slice(i, i + chunkSize);
    console.log("Saving batch:", batch);
  }
}

saveInChunks([1,2,3,4,5,6,7], 3);
// Saving [1,2,3] [4,5,6] [7]
```
</details>
3. Class vs Record in C#
<details> <summary>👉 Answer</summary>

Class: Reference type, mutable, equality by reference.
Record: Reference type, immutable by default, equality by value.

Example:
```cs
class PersonClass
{
    public string Name { get; set; }
}

record PersonRecord(string Name);

var c1 = new PersonClass { Name = "Sunil" };
var c2 = new PersonClass { Name = "Sunil" };
Console.WriteLine(c1.Equals(c2)); // False (different references)

var r1 = new PersonRecord("Sunil");
var r2 = new PersonRecord("Sunil");
Console.WriteLine(r1.Equals(r2)); // True (value equality)
```
</details>
4. Topic vs Queue in Azure
<details> <summary>👉 Answer</summary>

Queue: Point-to-point, one consumer processes a message.

Topic: Publish-subscribe, multiple subscribers can process copies.

Example:

Queue → Order service sends message → Only Billing service consumes.

Topic → Order service sends message → Billing + Notification + Analytics all receive.

</details>
5. CAP Theorem
<details> <summary>👉 Answer</summary>

CAP Theorem: A distributed system can provide only 2 out of 3 guarantees:

Consistency

Availability

Partition Tolerance

Example Systems:

CP: MongoDB (prioritize consistency over availability).

AP: Cassandra (available but may show stale data).

CA: Traditional relational DB (not partition tolerant).

</details>
6. SOLID Principles
<details> <summary>👉 Answer</summary>

S – Single Responsibility Principle

O – Open/Closed Principle

L – Liskov Substitution Principle

I – Interface Segregation Principle

D – Dependency Inversion Principle

Example (C#):
```cs
// Single Responsibility - Class only handles one job
public class ReportSaver {
    public void Save(string report) {
        Console.WriteLine("Report saved");
    }
}


Example (JavaScript - Dependency Inversion):

class MySQLDatabase {
  save(data) { console.log("Saving to MySQL:", data); }
}

class App {
  constructor(db) { this.db = db; }
  run() { this.db.save("data"); }
}

const app = new App(new MySQLDatabase());
app.run();
```
</details>
7. Dependency Injection
<details> <summary>👉 Answer</summary>

Definition: Providing dependencies from outside instead of creating inside.

C# Example:
```cs
public class Service
{
    private readonly IRepository _repo;
    public Service(IRepository repo) { _repo = repo; }
}
```

JavaScript Example:
```js
function UserService(repo) {
  this.repo = repo;
}

const mockRepo = { getUser: () => "Mock User" };
const service = new UserService(mockRepo);
console.log(service.repo.getUser()); // Mock User
```
</details>
8. useEffect vs useReducer in React
<details> <summary>👉 Answer</summary>

useEffect: For side effects like API calls, timers, subscriptions.

useReducer: For complex state management.

useEffect Example:
```js
import { useEffect, useState } from "react";

function FetchUsers() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("/api/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return <div>{users.length} Users</div>;
}


useReducer Example:

import { useReducer } from "react";

function counterReducer(state, action) {
  switch (action.type) {
    case "inc": return { count: state.count + 1 };
    case "dec": return { count: state.count - 1 };
    default: return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <button onClick={() => dispatch({ type: "inc" })}>+</button>
      <button onClick={() => dispatch({ type: "dec" })}>-</button>
      Count: {state.count}
    </div>
  );
}
```
</details>
9. Onion Architecture vs Clean Architecture
<details> <summary>👉 Answer</summary>

Onion Architecture: Layers are concentric circles. Domain is core, infrastructure is outer.

Clean Architecture: Similar but more generic, with use-cases around domain, then adapters, frameworks.

Diagram Idea:

Onion:         Clean:
Domain         Entities
App Services   Use Cases
Infra          Interface Adapters
UI             Frameworks


Example:

Onion: Repositories, Services, Controllers.

Clean: Entities, Use Cases, Presenters, Gateways.

</details>
10. Does MongoDB support Joins?
<details> <summary>👉 Answer</summary>

MongoDB doesn’t support joins like SQL, but you can use $lookup for similar functionality.

Example:
```db
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customerDetails"
    }
  }
])

MongoDB $lookup Detailed Explanation

The query:

db.orders.aggregate([
  {
    $lookup: {
      from: "customers",        // Collection to join with (customers)
      localField: "customerId", // Field in "orders"
      foreignField: "_id",      // Field in "customers"
      as: "customerDetails"     // Output array field
    }
  }
])

1. Collections Setup (Example Data)

orders collection

[
  { _id: 1, item: "Laptop", customerId: 101 },
  { _id: 2, item: "Phone", customerId: 102 },
  { _id: 3, item: "Tablet", customerId: 101 }
]


customers collection

[
  { _id: 101, name: "Alice", city: "New York" },
  { _id: 102, name: "Bob", city: "London" },
  { _id: 103, name: "Charlie", city: "Paris" }
]

2. What $lookup Does

It performs a left outer join between the orders collection and the customers collection.

It takes customerId from orders.

Looks for matching _id in customers.

Puts the matched docs inside a new array field customerDetails.

3. Output of the Query
[
  {
    _id: 1,
    item: "Laptop",
    customerId: 101,
    customerDetails: [
      { _id: 101, name: "Alice", city: "New York" }
    ]
  },
  {
    _id: 2,
    item: "Phone",
    customerId: 102,
    customerDetails: [
      { _id: 102, name: "Bob", city: "London" }
    ]
  },
  {
    _id: 3,
    item: "Tablet",
    customerId: 101,
    customerDetails: [
      { _id: 101, name: "Alice", city: "New York" }
    ]
  }
]

4. Important Points

$lookup always creates an array (customerDetails), even if one match is found.

If no match is found → customerDetails: [].

It’s similar to LEFT OUTER JOIN in SQL.

5. Flattening the Array ($unwind)

If you want only one customer object instead of an array:

db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customerDetails"
    }
  },
  { $unwind: "$customerDetails" }
])


👉 Output:

[
  { _id: 1, item: "Laptop", customerId: 101, customerDetails: { _id: 101, name: "Alice", city: "New York" } },
  { _id: 2, item: "Phone", customerId: 102, customerDetails: { _id: 102, name: "Bob", city: "London" } },
  { _id: 3, item: "Tablet", customerId: 101, customerDetails: { _id: 101, name: "Alice", city: "New York" } }
]

6. $lookup with Pipeline (More Powerful)

MongoDB 3.6+ allows using a pipeline for advanced joins.

Example: Match only customers from "New York":

db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      let: { orderCustId: "$customerId" },  // pass variable
      pipeline: [
        { $match: { $expr: { $eq: ["$_id", "$$orderCustId"] } } },
        { $match: { city: "New York" } }
      ],
      as: "customerDetails"
    }
  }
])


👉 Only orders from Alice (New York) will get joined.

7. $lookup vs SQL Join

Equivalent SQL:

SELECT o._id, o.item, c.name, c.city
FROM orders o
LEFT JOIN customers c
ON o.customerId = c._id;


✅ In short:

$lookup = MongoDB’s way of doing joins.

Output always has an array field.

Combine with $unwind and $project for clean results.

$lookup with pipeline = super powerful for filtering/joining multiple conditions.
```

This will join orders with customers.

</details>
