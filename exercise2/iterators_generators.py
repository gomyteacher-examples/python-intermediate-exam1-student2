class PrimeGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
        self.start = 2  # for reset method
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            num = self.current
            self.current += 1
            if self.is_prime(num):
                return num
        raise StopIteration
    
    def reset(self):
        """Reset the iterator to start from beginning"""
        self.current = self.start
    
    def is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        # check if divisible by any number up to n/2 - should be good enough
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True

def fibonacci_primes(n):
    """Generator that yields the first n numbers that are both Fibonacci and prime"""
    if n <= 0:
        return
    
    # generate fibonacci numbers and check if they're prime
    a, b = 0, 1
    primes_found = 0
    
    while primes_found < n:
        if is_prime_simple(a):
            yield a
            primes_found += 1
        a, b = b, a + b
        # prevent infinite loop - fibonacci gets very large
        if a > 1000000:  # reasonable limit for student code
            break

def is_prime_simple(n):
    if n < 2:
        return False
    # simple prime check - just divide by everything
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# decorator for caching - copied from stackoverflow
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
    # test prime generator
    primes = PrimeGenerator(20)
    prime_list = list(primes)
    print("Primes up to 20:", prime_list)
    
    # test reset method
    primes.reset()
    first_three = []
    for i, prime in enumerate(primes):
        if i >= 3:
            break
        first_three.append(prime)
    print("First 3 primes after reset:", first_three)
    
    # test fibonacci primes
    print("First 5 fibonacci primes:")
    fib_primes = list(fibonacci_primes(5))
    print(fib_primes)
    
    # test memoized fibonacci
    print("Fibonacci(10):", fibonacci(10))
    
    # bonus: try itertools
    from itertools import islice
    primes2 = PrimeGenerator(50)
    first_five = list(islice(primes2, 5))
    print("First 5 primes using islice:", first_five)
