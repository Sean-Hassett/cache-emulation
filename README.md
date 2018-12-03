####Cache Emulation

This Python class can be used to emulate a K-way cache and count cache hits and cache misses for a series of cache accesses.

Specify the number of sets(K), number of lines per set(N) and the number of bytes per line(L) when creating a Cache object.
You can then try to access a sequence of addresses and the cache will keep count of how many hits and misses there were.

See sample.py for an example of creating a cache and accessing a sequence of addresses. The output from sample.py should be:
```
K=1; N=8
HITS: 9
MISSES: 23
```