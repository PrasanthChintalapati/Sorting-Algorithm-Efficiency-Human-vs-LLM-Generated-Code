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
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        vis = [0] * 2001
        ans = 0
        for start, end, duration in tasks:
            covered = sum(vis[start : end + 1])
            remaining = duration - covered
            i = end
            while remaining > 0:
                if vis[i] == 0:
                    vis[i] = 1
                    ans += 1
                    remaining -= 1
                i -= 1
        return ans

solution = Solution()
test_cases = [
    ([[3, 7, 5], [3, 7, 1], [4, 10, 5], [10, 10, 1]]),
    ([[4, 5, 2], [5, 7, 3], [6, 7, 2], [9, 9, 1], [8, 10, 3]]),
    ([[1, 1, 1], [6, 7, 2], [1, 7, 7], [7, 9, 1], [7, 9, 3], [7, 10, 3], [10, 10, 1], [9, 10, 2], [1, 10, 5], [10, 10, 1]]),
    ([[3, 4, 2], [3, 5, 1], [1, 5, 4], [5, 5, 1], [5, 7, 3], [1, 7, 4], [1, 8, 7], [7, 8, 1], [5, 10, 1], [10, 10, 1]]),
    ([[1, 3, 2], [8, 8, 1], [3, 9, 5], [8, 10, 1]]),
    ([[2, 3, 1], [7, 8, 2], [8, 8, 1]]),
    ([[2, 8, 1], [7, 8, 1]]),
    ([[5, 7, 2], [9, 9, 1], [10, 10, 1]]),
    ([[2, 6, 1], [5, 7, 2], [10, 10, 1]]),
    ([[2, 2, 1], [6, 7, 1], [3, 8, 2], [4, 9, 2], [9, 9, 1], [4, 10, 5], [10, 10, 1], [10, 10, 1]]),
]

results = []
for tasks in test_cases:
    result = solution.findMinimumTime(tasks)
    results.append(result)

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.findMinimumTime(task_list) for task_list in test_cases]
)

for i, result in enumerate(results):
    print(f"Input: tasks={test_cases[i]}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")