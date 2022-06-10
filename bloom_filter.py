from bloom_filter2 import BloomFilter
from memory_profiler import profile
import uuid
import timeit


@profile
def test_insert_bloom(test_count, max_elements=10000, error_rate=0.1):
    bloom = BloomFilter(max_elements=max_elements, error_rate=error_rate)

    for _ in range(test_count):
        bloom.add(str(uuid.uuid4()))


def insert_bloom(test_count, max_elements=10000, error_rate=0.1):
    bloom = BloomFilter(max_elements=max_elements, error_rate=error_rate)

    for _ in range(test_count):
        bloom.add(str(uuid.uuid4()))

    return bloom


def insert_set(test_count):
    _set = set()
    for _ in range(test_count):
        _set.add(str(uuid.uuid4()))
    return _set


def test_read_set(test_count, set_):
    for _ in range(test_count):
        uuid_ = str(uuid.uuid4())
        uuid_ not in set_


def test_read_bloom(test_count, bloom_filter):
    for _ in range(test_count):
        uuid_ = str(uuid.uuid4())
        uuid_ not in bloom_filter


@profile
def test_insert_set(test_count):
    _set = set()
    for _ in range(test_count):
        _set.add(str(uuid.uuid4()))


if __name__ == '__main__':
    time_bloom = timeit.timeit(lambda: test_insert_bloom(1000000, max_elements=1000000, error_rate=0.1), number=1)
    # time_set = timeit.timeit(lambda: test_set(1000), number=1)
    print(time_bloom)
    # print(time_set)

    # bloom_filter = insert_bloom(10000)
    # time_read_bloom = timeit.timeit(lambda: test_read_bloom(10000, bloom_filter), number=1)
    # print(time_read_bloom)
    #
    # set_ = insert_set(10000)
    # time_read_set = timeit.timeit(lambda: test_read_set(10000, set_), number=1)
    # print(time_read_set)
