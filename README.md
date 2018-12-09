#### Cache Emulation

This Python class can be used to emulate a K-way cache and count cache hits and cache misses for a series of cache accesses.

Specify the number of sets(N), number of lines per set(K) and the number of bytes per line(L) when creating a Cache object.
You can then try to access a sequence of addresses and the cache will keep count of how many hits and misses there were.

See sample.py for an example of creating a cache and accessing a sequence of addresses. The output from sample.py should be:
```
K=1; N=8
HITS: 9
MISSES: 23
```

import sys

def hasEvenDigits(num):
    for c in num:
        if int(c) % 2 == 0:
            return True
    return False

for line in sys.stdin:
    
    original = int(line)
    reverse = int(line[::-1])
    
    sum_digits = original + reverse
    iterations = 1
    
    finished = not hasEvenDigits(str(sum_digits))
    while not finished:
        sum_digits = sum_digits + int(str(sum_digits)[::-1])
        iterations += 1
        finished = not hasEvenDigits(str(sum_digits)
        
    print(str(iterations) + " " + str(sum_digits), end="")
