import time
import tracemalloc
from bisect import bisect_right
from collections import defaultdict
from typing import List

# Solution class
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # Sort and deduplicate arr2
        arr2 = sorted(set(arr2))
        
        # dp[prev] = min operations to make current prefix strictly increasing with last value = prev
        dp = {0: 0}  # Key: prev value, Value: min operations
        n = len(arr1)
        
        for i in range(n):
            next_dp = defaultdict(lambda: float('inf'))
            curr = arr1[i]
            
            # For each previous value in dp
            for prev, cost in dp.items():
                # Case 1: Keep arr1[i] if it's greater than prev
                if curr > prev:
                    next_dp[curr] = min(next_dp[curr], cost)
                
                # Case 2: Replace arr1[i] with a value from arr2
                # Find smallest value in arr2 > prev
                idx = bisect_right(arr2, prev)
                for val in arr2[idx:]:
                    next_dp[val] = min(next_dp[val], cost + 1)
            
            dp = next_dp
            if not dp:
                return -1  # No valid solution at this step
        
        return min(dp.values()) if dp else -1

# Test cases execution
if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.perf_counter()
    
    solution = Solution()
    test_cases = [
        ([1,5,3,6,7], [1,3,2,4], 1),
        ([1,5,3,6,7], [4,3,1], 2),
        ([1,5,3,6,7], [1,6,3,3], -1),
        ([8,77,68,15,93,1,69,10,43], [11,43,75,98], -1),
        ([72,9,43,58,42,27], [11,22,64,68,86,87], 4),
        ([35,2,78,51,57,27,24,21,99], [15,54,56,65,68,72,100], -1),
        ([39,38,23,30,81,18,87,36,68], [7,49,55,58], -1),
        ([30,45,99,13,6,84,10,12,40,34], [2,11,15,18,22,55,90,96], -1),
        ([44,97,15,17,47], [5,14,23,33,37,69,80,84], 2),
        ([36,25,99,45], [4,24,39,47,62,79,84,89,96], 2),
        ([24,95,91,36], [24,42,49,54,61,77,85,93,96], 2),
        ([7,46], [1,17,26,39,42,63,66,68,81,91], 0),
        ([26,4,97], [2,22,30,34,38,55,73,84,90], 1)
    ]
    
    for i, (arr1, arr2, expected) in enumerate(test_cases, 1):
        result = solution.makeArrayIncreasing(arr1, arr2)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: arr1={arr1}, arr2={arr2}, output={result}")
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    execution_time_s = end_time - start_time
    peak_memory_mb = peak / (1024 * 1024)
    print(f"\nExecution Time: {execution_time_s:.6f} seconds")
    print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
    tracemalloc.stop()