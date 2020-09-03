#!/usr/bin/env python3

from FibonacciHeap import FibonacciHeap
from HollowHeap import HollowHeap

nodes = [(10,"a"),(4,"b"),(295,"c"),(42,"d"),(85,"e"),(1,"f"),(23,"g")]

# to store the nodes
f = [None] * len(nodes)
h = [None] * len(nodes)

fib1 = FibonacciHeap()
hol1 = HollowHeap()

fib2 = FibonacciHeap()
hol2 = HollowHeap()

for i in range(len(nodes)):
    if i < 4:
        f[i] = fib1.insert(nodes[i][0], nodes[i][1])
        h[i] = hol1.insert(nodes[i][0], nodes[i][1])
    else:
        f[i] = fib2.insert(nodes[i][0], nodes[i][1])
        h[i] = hol2.insert(nodes[i][0], nodes[i][1])

print("should be 'b'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

fib1.delete_min()
hol1.delete_min()
print("should be 'a'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

fib1.union(fib2)
hol1.union(hol2)
print("should be 'f'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

fib1.delete_min()
hol1.delete_min()
print("should be 'a'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

# decrease (23, g) to (1, g)
fib1.decrease_key(f[6], 1)
hol1.decrease_key(h[6], 1)
print("should be 'g'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

fib1.delete_min()
hol1.delete_min()
print("should be 'a'")
print("fibonacci heap: %s, hollow heap: %s\n"
    % (fib1.min().value, hol1.min().item))

# delete (42, d)
fib1.delete(f[3])
hol1.delete(h[3])
fib1.delete_min()
hol1.delete_min()
print("should be 'e'")
print("fibonacci heap: %s, hollow heap: %s"
    % (fib1.min().value, hol1.min().item))


# correct output
'''
should be 'b'
fibonacci heap: b, hollow heap: b 

should be 'a'        
fibonacci heap: a, hollow heap: a

should be 'f'
fibonacci heap: f, hollow heap: f

should be 'a'
fibonacci heap: a, hollow heap: a

should be 'g'
fibonacci heap: g, hollow heap: g

should be 'a'
fibonacci heap: a, hollow heap: a

should be 'e'
fibonacci heap: e, hollow heap: e
'''
