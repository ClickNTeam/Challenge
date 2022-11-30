# Solution Writeup

## 1. Data analysis

First step before approaching the problem is analysing, understanding duplicates,
and finding if there is a key to consider, in the end there was no key like and i chose the index of element in the list.

## 2. Choosing a solution

I choose to build a recommendation graph due it's O(1) search complexity and how easy adding an item to it.

## 3. Implementing the graph

I choose to create a class for the graph with all the CRUD needed to plug it into any system, an API for example.

## 4. limitation and possible improvements

- The biggest limitation is creating the whole graph which takes relatively much time this is because of the size of data, python performance.

	This can be mitigated by using better algorithms (divide and conquer for the price filtering), we can also gain much performance by Implementing multithreaded although this would need more time.

- This can be implemented as is in production or by using mongodb which is a very popular choice for graph databases.
