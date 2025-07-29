import sys
import time

sys.setrecursionlimit(10**7)

def slow_fib(n):
    if n <= 1:
        return n
    return slow_fib(n-1) + slow_fib(n-2)

if __name__ == "__main__":
    start = time.time()
    n = 35  # This value is big enough to slow down low-end PCs
    print(f"Calculating Fibonacci number for n={n} (slowly)...")
    result = slow_fib(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result}")
    print(f"Time taken: {end - start:.2f} seconds")
