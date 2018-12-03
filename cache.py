from math import log


class Cache:
    def __init__(self, L, K, N):
        """
        Initialise a Cache object with a cache represented as a 2D array and a 3D array used to get a true LRU
        :param L: Number of bytes per line
        :param K: Number of lines per set
        :param N: Number of sets
        """
        self.L = L
        self.K = K
        self.N = N
        self.cache = []
        self.LRU_matrices = []
        for i in range(self.N):
            matrix = []
            for j in range(self.K):
                matrix.append([False] * self.K)
            self.LRU_matrices.append(matrix)
        for i in range(self.N):
            self.cache.append([-1] * self.K)

        self.hits = 0
        self.misses = 0

    def get_set_number(self, addr):
        """
        Get the set number from the address that is being looked up
        :param addr: Address that is being accessed
        :return: The set number as an int derived from part or all of the 3rd hexadecimal digit
        """
        set_number = addr & 0x00f0
        set_number >>= 4
        set_number <<= (4 - int((log(self.N, 2))))
        set_number &= 0x000f
        set_number >>= (4 - int((log(self.N, 2))))
        return set_number

    def get_cache_offset(self, addr):
        """
        Get the offset into the cache line from the address that is being looked up
        :param addr: Address that is being accessed
        :return: The cache offset as an int derived from the 4th hexadecimal digit
        """
        return addr & 0x000f

    def get_tag(self, addr):
        """
        Get the tag from the address that is being looked up
        :param addr: Address that is being accessed
        :return: The tag as an int derived from the most significant bits up to the start of the set number
        """
        hexN = addr
        hexN >>= (4 + int((log(self.N, 2))))
        return hexN

    def access_cache(self, addr):
        """
        Look up the address in the cache. On hit, increment the hits counter and update the LRU. On miss,
        update the misses counter and add the address to the cache
        :param addr: Address that is being accessed
        :return: null
        """
        set_number = self.get_set_number(addr)
        tag = self.get_tag(addr)
        for r in range(len(self.cache[set_number])):
            if self.cache[set_number][r] == tag:
                self.hits += 1
                self.update_LRU(set_number, r)
                return
        self.misses += 1
        self.store(tag, set_number)

    def store(self, tag, set_number):
        """
        Store a tag in the cache and update the least recently used line
        :param tag: The tag to be stored in the cache
        :param set_number: The index of the set where the tag should be stored
        :return: null
        """
        LRU_line = self.get_LRU_line(set_number)
        self.cache[set_number][LRU_line] = tag
        self.update_LRU(set_number, LRU_line)

    def get_LRU_line(self, set_number):
        """
        Get the line in the given set which is the least recently used
        :param set_number: The index of the set that is being queried
        :return: The index of the line which is the least recently used in the set
        """
        for r in range(len(self.LRU_matrices[set_number])):
            if not any(self.LRU_matrices[set_number][r]):
                return r

    def update_LRU(self, set_number, LRU_line):
        """
        Update the LRU matrix to reflect accesses to the cache. Called on a cache hit or when storing a new
        address in the cache
        :param set_number: The index of the set that is being updated
        :param LRU_line: The index of the line which is has just been accessed
        :return: null
        """
        self.LRU_matrices[set_number][LRU_line] = [True] * len(self.LRU_matrices[set_number][LRU_line])
        for row in self.LRU_matrices[set_number]:
            row[LRU_line] = False
