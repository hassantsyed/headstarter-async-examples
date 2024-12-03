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

# Distributed version using multiprocessing
from multiprocessing import Pool

def find_primes_distributed(total_range, num_workers=4):
    # Ensure even distribution of work
    start, end = total_range
    chunk_size = max(1000, (end - start + num_workers - 1) // num_workers)  # Minimum chunk size of 1000
    ranges = []
    
    current = start
    while current < end:
        next_end = min(current + chunk_size, end)
        ranges.append((current, next_end))
        current = next_end
    
    # Distribute the work across processes
    with Pool(num_workers) as pool:
        results = pool.starmap(find_primes_single, ranges)
    
    return [prime for sublist in results for prime in sublist]

if __name__ == "__main__":
    import time
    
    # Use a larger range to better demonstrate the benefit
    range_to_check = (1, 1000000)  # Increased to 1 million
    
    # Single process
    start = time.time()
    single_results = find_primes_single(*range_to_check)
    single_time = time.time() - start
    print(f"Single process took: {single_time:.2f} seconds")
    
    # Distributed
    start = time.time()
    distributed_results = find_primes_distributed(range_to_check)
    distributed_time = time.time() - start
    print(f"Distributed took: {distributed_time:.2f} seconds")
    
    print(f"Speedup: {single_time/distributed_time:.2f}x")
    print(f"Found {len(single_results)} primes")