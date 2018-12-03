from cache import Cache

input_data = [0x0000, 0x0004, 0x000c, 0x2200, 0x00d0, 0x00e0, 0x1130, 0x0028,
              0x113c, 0x2204, 0x0010, 0x0020, 0x0004, 0x0040, 0x2208, 0x0008,
              0x00a0, 0x0004, 0x1104, 0x0028, 0x000c, 0x0084, 0x000c, 0x3390,
              0x00b0, 0x1100, 0x0028, 0x0064, 0x0070, 0x00d0, 0x0008, 0x3394]

L = 16
cache = Cache(L, 1, 8)

for addr in input_data:
    cache.access_cache(addr)

print("K={}; N={}".format(cache.K, cache.N))
print("HITS: {}".format(cache.hits))
print("MISSES: {}\n".format(cache.misses))
