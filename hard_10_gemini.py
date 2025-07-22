from typing import List
import bisect
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
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            start_day, end_day, value = events[i - 1]
            prev_event_index = bisect.bisect_left(events, start_day, hi=i - 1, key=lambda x: x[1])
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[prev_event_index][j - 1] + value)
        return dp[n][k]

solution = Solution()
test_cases = [
    ([[16, 37, 6], [49, 93, 7]], 2),
    ([[8, 42, 2], [29, 47, 1], [43, 67, 2], [22, 67, 3], [48, 68, 3], [62, 78, 7], [39, 90, 5], [38, 97, 5], [74, 98, 7], [90, 99, 2]], 1),
    ([[56, 66, 2], [71, 82, 7], [91, 94, 6]], 3),
    ([[7, 32, 9], [44, 63, 5], [46, 79, 1], [83, 85, 1], [90, 90, 10], [80, 97, 9], [87, 98, 5], [88, 99, 3]], 8),
    ([[25, 40, 6], [12, 58, 4], [47, 65, 10], [49, 80, 2], [67, 87, 5], [87, 96, 4], [97, 99, 6]], 6),
    ([[16, 28, 6], [88, 92, 4], [21, 92, 1], [94, 100, 3], [56, 100, 3], [2, 100, 3]], 4),
    ([[19, 39, 1], [26, 65, 7], [43, 71, 2], [67, 75, 10], [76, 97, 10], [40, 98, 2], [97, 99, 4], [79, 99, 8]], 8),
    ([[34, 49, 7], [4, 84, 1], [87, 95, 5], [96, 98, 9]], 1),
    ([[2, 19, 8], [31, 54, 5]], 2),
    ([[2, 20, 1], [23, 23, 10], [23, 32, 5], [51, 52, 5], [56, 65, 10], [65, 79, 2], [44, 82, 10], [71, 88, 7], [18, 96, 9], [41, 99, 3]], 3),
]

results = []
for events, k in test_cases:
    result = solution.maxValue(events, k)
    results.append(result)

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.maxValue(ev, kk) for ev, kk in test_cases]
)

for i, result in enumerate(results):
    events, k = test_cases[i]
    print(f"Input: events={events}, k={k}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")