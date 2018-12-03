from cache import Cache


def testInit():
    c = Cache(16, 2, 4)
    assert c.L == 16
    assert c.K == 2
    assert c.N == 4
    assert c.cache == [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    assert c.LRU_matrices == [[[False, False], [False, False]],
                              [[False, False], [False, False]],
                              [[False, False], [False, False]],
                              [[False, False], [False, False]]]


def test_get_set_number():
    c = Cache(16, 2, 4)
    assert c.get_set_number(0x0000) == 0
    assert c.get_set_number(0x113c) == 3


def test_get_cache_offset():
    c = Cache(16, 1, 8)
    assert c.get_cache_offset(0x0084) == 4
    assert c.get_cache_offset(0x113c) == 12


def test_get_tag():
    c = Cache(16, 4, 2)
    assert c.get_tag(0x0000) == 0x000
    assert c.get_tag(0x2200) == 0x110
    assert c.get_tag(0x113c) == 0x089


def test_access_cache():
    c = Cache(16, 4, 2)
    c.access_cache(0x0000)
    assert c.hits == 0
    assert c.misses == 1
    c.access_cache(0x0000)
    assert c.hits == 1
    assert c.misses == 1


def test_store():
    c = Cache(16, 4, 2)
    c.store(0x112, 1)
    assert c.cache == [[-1, -1, -1, -1], [0x112, -1, -1, -1]]


def test_get_LRU_line():
    c = Cache(16, 2, 4)
    assert c.get_LRU_line(0) == 0
    c.update_LRU(0, 0)
    assert c.get_LRU_line(0) == 1
    c.update_LRU(0, 1)
    assert c.get_LRU_line(0) == 0


def test_update_LRU():
    c = Cache(16, 2, 4)
    c.update_LRU(2, 0)
    assert c.LRU_matrices == [[[False, False], [False, False]],
                              [[False, False], [False, False]],
                              [[False, True], [False, False]],
                              [[False, False], [False, False]]]
