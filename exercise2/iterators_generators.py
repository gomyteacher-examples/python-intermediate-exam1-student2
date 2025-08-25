class PrimeGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            num = self.current
            self.current += 1
            if self.is_prime(num):
                return num
        raise StopIteration
    
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):  # i think this works?
            if n % i == 0:
                return False
        return True

def fibonacci_primes(n):
    # make fibonacci numbers first
    fib_nums = []
    a, b = 0, 1
    
    while len(fib_nums) < 100:  # should be enough
        fib_nums.append(a)
        a, b = b, a + b
    
    primes_found = 0
    for fib in fib_nums:
        if is_prime_simple(fib) and primes_found < n:
            yield fib
            primes_found += 1

def is_prime_simple(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# decorator for caching
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    primes = PrimeGenerator(20)
    prime_list = list(primes)
    print("Primes up to 20:", prime_list)
    
    print("First 5 fibonacci primes:")
    for fp in fibonacci_primes(5):
        print(fp)
    
    print("Fibonacci(10):", fibonacci(10))
