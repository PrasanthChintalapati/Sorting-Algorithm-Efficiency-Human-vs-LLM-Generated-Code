from typing import List
from bisect import bisect_left
import time
import tracemalloc

# Solution class (same as above)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start, _, value) in enumerate(events, 1):
            p = bisect_left(events, start, hi=i-1, key=lambda x: x[1])
            for j in range(k + 1):
                f[i][j] = f[i-1][j]
                if j > 0:
                    f[i][j] = max(f[i][j], f[p][j-1] + value)
        return f[n][k]

# Start memory and time tracking
tracemalloc.start()
start_time = time.perf_counter()

# Initialize solution
solution = Solution()

# Test cases
test_cases = [
    ([[16, 37, 6], [49, 93, 7]], 2, 13),
    ([[8, 42, 2], [29, 47, 1], [43, 67, 2], [22, 67, 3], [48, 68, 3], [62, 78, 7], [39, 90, 5], [38, 97, 5], [74, 98, 7], [90, 99, 2]], 1, 7),
    ([[56, 66, 2], [71, 82, 7], [91, 94, 6]], 3, 15),
    ([[7, 32, 9], [44, 63, 5], [46, 79, 1], [83, 85, 1], [90, 90, 10], [80, 97, 9], [87, 98, 5], [88, 99, 3]], 8, 25),
    ([[25, 40, 6], [12, 58, 4], [47, 65, 10], [49, 80, 2], [67, 87, 5], [87, 96, 4], [97, 99, 6]], 6, 27),
    ([[16, 28, 6], [88, 92, 4], [21, 92, 1], [94, 100, 3], [56, 100, 3], [2, 100, 3]], 4, 13),
    ([[19, 39, 1], [26, 65, 7], [43, 71, 2], [67, 75, 10], [76, 97, 10], [40, 98, 2], [97, 99, 4], [79, 99, 8]], 8, 27),
    ([[34, 49, 7], [4, 84, 1], [87, 95, 5], [96, 98, 9]], 1, 9),
    ([[2, 19, 8], [31, 54, 5]], 2, 13),
    ([[2, 20, 1], [23, 23, 10], [23, 32, 5], [51, 52, 5], [56, 65, 10], [65, 79, 2], [44, 82, 10], [71, 88, 7], [18, 96, 9], [41, 99, 3]], 3, 27)
]

# Run test cases
for i, (events, k, expected) in enumerate(test_cases, 1):
    result = solution.maxValue(events, k)
    assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print(f"Test case {i} passed: Output={result}")

# Calculate and print execution time and memory usage
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)

print(f"\nExecution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
tracemalloc.stop()