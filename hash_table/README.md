## Hashtables
- A hash map is a data structure that implements a set abstract data type, a structure that can map keys to values.

### Challenge
- Implement a Hashtable Class with the following methods:

1- set
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

2- get
- Arguments: key
- Returns: Value associated with that key in the table

3- contains
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

4- keys
- Returns: Collection of keys

5- hash
- Arguments: key
- Returns: Index in the collection for that key

#### Approach & Efficiency

- The only method that has a for loop is the get and contains methods which takes a linear iterative approach.

1- set
- Time: Big O(1)
- Space: Big O(n)

1- get
- Time: Big O(n)
- Space: Big O(n)

1- contains
- Time: Big O(n)
- Space: Big O(n)

1- keys 
- Time: Big O(1)
- Space: Big O(1)

1- hash
- Time: Big O(1)
- Space: Big O(1)

#### API

I've implemented the following methods in Hashtable class:

- set(): to inserts data to the hash table.
- get(): to gets value of the required key with collision handled.
- contains(): returns true or false if the key is in the hashed table or not
- keys(): returns a collection of all the existed keys in the hashed table.