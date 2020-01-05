# Fibonacci and Hollow Heaps
This contains python implementations of Fibonacci and Hollow Heaps. Both datastructures store `(key, value)` pairs and offer fast removal of the pair with minimal key. Fibonacci heaps were invented in the 1980s with the goal of makin Djikstra's algorithm faster. Hollow Heaps are a more recent datastructure, invented in 2015 with the goal of making Fibonacci heaps easier to implement.


# Functions
Both datastructures implement the following heap functions: `insert`, `min`, `union`, `delete_min`, `decrease_key` and `delete`. In both datastructures all of the functions run in amortized constant time except for `delete_min` and `delete` which have amortized complexity of `O(log n)`.


# Documentation
Short documentation on how each of the functions work.
## Initialize
Initializes a empty heap.
```python
h = HollowHeap()
f = FibonacciHeap()
```

## Insert
Given a integer key and arbitrary value, it returns the node created in the data structure for later use.
```python
h.insert(10, "value")
f.insert(10, "value")
```

## Min
Returns the node with minimal key.
```python
h.min()
f.min()
```

## Union
Merges two heaps
```python
h.union(other)
f.union(other)
```

## Delete minimum
Deletes the node with minimal key and returns it
```python
h.delete_min()
f.delete_min()
```

## Decrease key
Given a node and a new key, it sets the key of the node to the new one
```python
h.decrease_key(node, 1)
f.decrease_key(node, 1)
```

## Delete
Given a node the function removes it from the heap and returns the deleted node.
```python
h.delete(node)
f.delete(node)
```
