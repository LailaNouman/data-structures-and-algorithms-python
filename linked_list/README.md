# Singly Linked List

A singly linked list can be traversed in only one direction from head to the last node (tail). Each element in a linked list is called a node. A single node contains data and a pointer to the next node.

## Challenge:

Create a linked list class and include a head property and the class has methods like (insert, includes, toString) 

## Challenge 2:

append: adds a new node with the given value to the end of the list
insert before: adds a new node with the given new value immediately before the first node that has the value specified
insert after: adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard

![linkedlist](Untitled%20(2).jpg)


## Approach & Efficiency

Time complexity: 
- insert: Big O(1) 
- includes: Big O(N) 
- toString: Big O(N) 
- append: Big O(N) 
- insert before: Big O(N)  
- insert after: Big O(N)

I created two classes first class called Node and the second class called LinkedList the Node class creates 
a node that points to null. The LinkedList class has 6 methods each one of them doing a different thing to
the list so the insert method inserts a value inside the list, the append method adds a value to the end of
the list, the insert after method inserts a value after a specific element.

## API

- Insert: To insert values.
- Include: To check if a specific value exists in the list.
- Tostring: To print the list in a formatted way.
- Append: add to the last.
- Insert_before: to add an element before a specific element.
- Insert_after: to add an element after a specific element.