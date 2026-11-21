import sys, tracemalloc

sys.setrecursionlimit(10000)

def normal_rec(n):
    if n == 0:
        return tracemalloc.get_traced_memory()
    return normal_rec(n - 1)

def gen_rec(n):
    if n == 0:
        yield tracemalloc.get_traced_memory()
        return
    yield from gen_rec(n - 1)

tracemalloc.start(1)
print("Normal (n=1000):", normal_rec(1000))
tracemalloc.stop()

tracemalloc.start(1)
print("Generator (n=1000):", next(gen_rec(1000)))
tracemalloc.stop()

# output: 
# Normal (n=1000): (23776, 23776)
# Generator (n=1000): (223976, 223976)
