# io_bound.py

import time
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def fetch_slow_api() -> Tuple[int, str]:
    """Make a request to our slow API and return the status code."""
    try:
        print("Starting request...")
        response = requests.get('http://localhost:5001')
        response.raise_for_status()
        try:
            result = response.json()
            print(f"Request completed: {result}")
            return response.status_code, result['message']
        except ValueError as e:
            print(f"JSON decode error. Response text: {response.text}")
            return -1, f"Invalid JSON response: {str(e)}"
    except requests.RequestException as e:
        print(f"Request error: {str(e)}")
        return -1, str(e)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return -1, str(e)

def fetch_multiple_single(n: int) -> List[Tuple[int, str]]:
    """Make n requests sequentially."""
    return [fetch_slow_api() for _ in range(n)]

def fetch_multiple_threaded(n: int, num_threads: int = 4) -> List[Tuple[int, str]]:
    """Make n requests using multiple threads."""
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        return list(executor.map(lambda _: fetch_slow_api(), range(n)))

if __name__ == "__main__":
    num_requests = 4
    
    # Single-threaded execution
    print(f"\nMaking {num_requests} sequential requests...")
    start = time.time()
    single_results = fetch_multiple_single(num_requests)
    single_time = time.time() - start
    print(f"Single-threaded took: {single_time:.2f} seconds")

    # Multi-threaded execution
    print(f"\nMaking {num_requests} concurrent requests...")
    start = time.time()
    threaded_results = fetch_multiple_threaded(num_requests)
    threaded_time = time.time() - start
    print(f"Multi-threaded took: {threaded_time:.2f} seconds")

    print(f"\nSpeedup: {single_time/threaded_time:.2f}x")