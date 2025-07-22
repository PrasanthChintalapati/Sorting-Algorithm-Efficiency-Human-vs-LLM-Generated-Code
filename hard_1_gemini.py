import bisect
from math import inf
from typing import List
import time
import tracemalloc

def measure_execution(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time_s = end_time - start_time
    peak_memory_mb = peak / (1024 * 1024)
    return result, execution_time_s, peak_memory_mb

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))
        n = len(arr1)
        dp = {}

        def solve(index, prev):
            if index == n:
                return 0
            if (index, prev) in dp:
                return dp[(index, prev)]

            cost = inf
            # Option 1: Keep the current element
            if arr1[index] > prev:
                cost = min(cost, solve(index + 1, arr1[index]))

            # Option 2: Replace the current element with an element from arr2
            i = bisect.bisect_right(arr2, prev)
            if i < len(arr2):
                cost = min(cost, 1 + solve(index + 1, arr2[i]))

            dp[(index, prev)] = cost
            return cost

        result = solve(0, -1)
        return result if result != inf else -1

solution = Solution()

test_cases = [
    ([8, 77, 68, 15, 93, 1, 69, 10, 43], [11, 43, 75, 98]),
    ([72, 9, 43, 58, 42, 27], [11, 22, 64, 68, 86, 87]),
    ([35, 2, 78, 51, 57, 27, 24, 21, 99], [15, 54, 56, 65, 68, 72, 100]),
    ([39, 38, 23, 30, 81, 18, 87, 36, 68], [7, 49, 55, 58]),
    ([30, 45, 99, 13, 6, 84, 10, 12, 40, 34], [2, 11, 15, 18, 22, 55, 90, 96]),
    ([44, 97, 15, 17, 47], [5, 14, 23, 33, 37, 69, 80, 84]),
    ([36, 25, 99, 45], [4, 24, 39, 47, 62, 79, 84, 89, 96]),
    ([24, 95, 91, 36], [24, 42, 49, 54, 61, 77, 85, 93, 96]),
    ([7, 46], [1, 17, 26, 39, 42, 63, 66, 68, 81, 91]),
    ([26, 4, 97], [2, 22, 30, 34, 38, 55, 73, 84, 90]),
]

results = []
for arr1, arr2 in test_cases:
    result = solution.makeArrayIncreasing(arr1, arr2)
    results.append((arr1, arr2, result))

execution_result, execution_time, memory_usage = measure_execution(lambda: [solution.makeArrayIncreasing(arr1, arr2) for arr1, arr2 in test_cases])

for arr1, arr2, result in results:
    print(f"Input: arr1={arr1}, arr2={arr2}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {memory_usage:.6f} MB")