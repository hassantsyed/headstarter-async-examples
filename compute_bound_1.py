# prime_calculator.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Non-distributed version - compute bound
def find_primes_single(start, end):
    return [n for n in range(start, end) if is_prime(n)]

if __name__ == "__main__":
    import time
    
    # Use a larger range to better demonstrate the benefit
    range_to_check = (1, 1000000)  # Increased to 1 million
    
    # Single process
    start = time.time()
    single_results = find_primes_single(*range_to_check)
    single_time = time.time() - start
    print(f"Single process took: {single_time:.2f} seconds")

    print(f"Found {len(single_results)} primes")