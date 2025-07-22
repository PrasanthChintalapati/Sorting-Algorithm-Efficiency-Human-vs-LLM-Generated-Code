import time
import tracemalloc
from bisect import bisect_left
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        from math import inf

        dp = {-1: 0}
        for num in arr1:
            new_dp = {}
            for prev in dp:
                if num > prev:
                    new_dp[num] = min(new_dp.get(num, inf), dp[prev])
                idx = bisect_left(arr2, prev + 1)
                if idx < len(arr2):
                    new_dp[arr2[idx]] = min(new_dp.get(arr2[idx], inf), dp[prev] + 1)
            dp = new_dp
            if not dp:
                return -1
        return min(dp.values())

# Start timing and memory tracking
tracemalloc.start()
start_time = time.perf_counter()

# Provided test cases
solution = Solution()
assert solution.makeArrayIncreasing([8, 77, 68, 15, 93, 1, 69, 10, 43], [11, 43, 75, 98]) == -1
assert solution.makeArrayIncreasing([72, 9, 43, 58, 42, 27], [11, 22, 64, 68, 86, 87]) == 4
assert solution.makeArrayIncreasing([35, 2, 78, 51, 57, 27, 24, 21, 99], [15, 54, 56, 65, 68, 72, 100]) == -1
assert solution.makeArrayIncreasing([39, 38, 23, 30, 81, 18, 87, 36, 68], [7, 49, 55, 58]) == -1
assert solution.makeArrayIncreasing([30, 45, 99, 13, 6, 84, 10, 12, 40, 34], [2, 11, 15, 18, 22, 55, 90, 96]) == -1
assert solution.makeArrayIncreasing([44, 97, 15, 17, 47], [5, 14, 23, 33, 37, 69, 80, 84]) == 2
assert solution.makeArrayIncreasing([36, 25, 99, 45], [4, 24, 39, 47, 62, 79, 84, 89, 96]) == 2
assert solution.makeArrayIncreasing([24, 95, 91, 36], [24, 42, 49, 54, 61, 77, 85, 93, 96]) == 2
assert solution.makeArrayIncreasing([7, 46], [1, 17, 26, 39, 42, 63, 66, 68, 81, 91]) == 0
assert solution.makeArrayIncreasing([26, 4, 97], [2, 22, 30, 34, 38, 55, 73, 84, 90]) == 1

# Stop timing and memory tracking
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Output
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)
print("All test cases passed.")
print(f"Execution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
