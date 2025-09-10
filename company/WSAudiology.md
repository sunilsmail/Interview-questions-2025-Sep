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
```

This will join orders with customers.

</details>
