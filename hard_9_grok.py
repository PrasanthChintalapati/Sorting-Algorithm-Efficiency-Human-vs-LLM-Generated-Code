from typing import List
import time
import tracemalloc

# Solution class (same as above)
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        vis = [False] * 2010
        ans = 0
        for start, end, duration in tasks:
            covered = sum(vis[start:end + 1])
            duration -= covered
            i = end
            while i >= start and duration > 0:
                if not vis[i]:
                    vis[i] = True
                    duration -= 1
                    ans += 1
                i -= 1
        return ans

# Start memory and time tracking
tracemalloc.start()
start_time = time.perf_counter()

# Initialize solution
solution = Solution()

# Test cases
test_cases = [
    ([[3, 7, 5], [3, 7, 1], [4, 10, 5], [10, 10, 1]], 6),
    ([[4, 5, 2], [5, 7, 3], [6, 7, 2], [9, 9, 1], [8, 10, 3]], 7),
    ([[1, 1, 1], [6, 7, 2], [1, 7, 7], [7, 9, 1], [7, 9, 3], [7, 10, 3], [10, 10, 1], [9, 10, 2], [1, 10, 5], [10, 10, 1]], 10),
    ([[3, 4, 2], [3, 5, 1], [1, 5, 4], [5, 5, 1], [5, 7, 3], [1, 7, 4], [1, 8, 7], [7, 8, 1], [5, 10, 1], [10, 10, 1]], 8),
    ([[1, 3, 2], [8, 8, 1], [3, 9, 5], [8, 10, 1]], 6),
    ([[2, 3, 1], [7, 8, 2], [8, 8, 1]], 3),
    ([[2, 8, 1], [7, 8, 1]], 1),
    ([[5, 7, 2], [9, 9, 1], [10, 10, 1]], 4),
    ([[2, 6, 1], [5, 7, 2], [10, 10, 1]], 3),
    ([[2, 2, 1], [6, 7, 1], [3, 8, 2], [4, 9, 2], [9, 9, 1], [4, 10, 5], [10, 10, 1], [10, 10, 1]], 6)
]

# Run test cases
for i, (tasks, expected) in enumerate(test_cases, 1):
    result = solution.findMinimumTime(tasks)
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