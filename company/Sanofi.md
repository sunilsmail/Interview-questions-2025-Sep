CloudStorage System — Summary of Methods & Functionality
You built a multi-level in-memory cloud storage system with:
File management
User storage limits
File copying
File search
Capacity management
Compression & decompression
Data Structures
Files
JavaScript
this.files = {
   "/dir/file.txt": {
      size: 10,
      userId: "user1"
   }
}
Each file stores:
size
userId
null → system/admin file
"user1" → owned by user
Users
JavaScript
this.users = {
   "user1": {
      capacity: 100,
      used: 40
   }
}
Each user stores:
total capacity
used storage
LEVEL 1 — Basic File Operations
1. addFile(path, size)
Purpose
Adds a system file.
Returns
true → success
false → file already exists
Example
JavaScript
addFile("/dir/file.txt", 10)
Stores:
JavaScript
{
  size: 10,
  userId: null
}
2. copyFile(fromPath, toPath)
Purpose
Copies existing file.
Rules
Fails if:
source missing
destination already exists
user capacity exceeded
User-owned files
copied under same owner
increase user storage usage
System files
can be copied freely
Returns
true
false
3. findFile(prefix, suffix)
Purpose
Find files matching:
path starts with prefix
path ends with suffix
Returns
JavaScript
[
  "/dir/file.txt(10)"
]
Sorting
Descending size
Lexicographical order
LEVEL 2 — Users & Capacity
4. addUser(userId, capacity)
Purpose
Creates new user.
Returns
true
false if user exists
5. addFileBy(userId, path, size)
Purpose
Adds file owned by user.
Rules
Fails if:
user missing
file exists
capacity exceeded
Returns
remaining capacity
null on failure
Example
JavaScript
addUser("user", 100)

addFileBy("user", "/a.txt", 40)
Returns:
JavaScript
60
LEVEL 3 — Capacity Updates
6. updateCapacity(userId, capacity)
Purpose
Changes user storage limit.
If current usage exceeds capacity:
Remove largest files first.
Removal Sorting
Largest size first
Lexicographical order
Returns
number of removed files
null if user missing
LEVEL 4 — Compression
7. compressFile(userId, name)
Purpose
Compress user-owned file.
Rules
Original:
JavaScript
"/a.txt"
Becomes:
JavaScript
"/a.txt.COMPRESSED"
Size
Compressed size = original size / 2
Fails if:
user missing
file missing
not owned by user
compressed file already exists
Returns
remaining capacity
null
8. decompressFile(userId, name)
Purpose
Restores compressed file.
Rules
Original:
JavaScript
"/a.txt.COMPRESSED"
Restores:
JavaScript
"/a.txt"
Size
Restored size = compressed size * 2
Fails if:
user missing
file missing
not .COMPRESSED
not owned by user
original file already exists
capacity exceeded
Returns
remaining capacity
null
Important Edge Cases Solved
Duplicate file prevention
JavaScript
if (this.files[path] !== undefined)
Capacity validation
JavaScript
if (user.used + size > user.capacity)
Proper sorting
JavaScript
b.size - a.size
then:
JavaScript
a.path.localeCompare(b.path)
Correct return format
JavaScript
"/dir/file.txt(10)"
NOT object arrays.
Final Functionalities Achieved
✅ Add files
✅ Copy files
✅ Search files
✅ User ownership
✅ Capacity tracking
✅ Capacity updates
✅ Compression
✅ Decompression
✅ Edge case handling
✅ Sorting logic
✅ Hidden testcase handling