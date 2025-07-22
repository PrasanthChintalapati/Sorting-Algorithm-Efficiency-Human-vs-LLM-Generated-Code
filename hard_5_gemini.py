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
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(profit)
        dp = [0] * (n + 1)
        for i, (e, s, p) in enumerate(jobs):
            j = bisect.bisect_right(jobs, s, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[j] + p)
        return dp[n]

solution = Solution()
test_cases = [
    ([788, 846, 685, 926, 120, 892, 426, 144, 67, 885], [376, 218, 161, 774, 474], [7594, 3954, 6603, 4847, 1229]),
    ([614, 238, 89], [28, 776, 834, 124, 439], [9203, 5748, 1333, 4358, 5075, 7922, 7958]),
    ([358, 742, 446, 70], [921, 546, 793], [9103, 2328, 1233, 55, 8593, 9166, 2855]),
    ([32, 989, 188, 863, 117], [807, 271, 229, 920, 225, 446], [613, 5471, 3971, 8692, 6863, 2314, 3201, 4057, 1207, 7937]),
    ([667, 941, 125, 840], [268, 545], [4882, 5023, 3029, 2727, 5899, 757]),
    ([899, 613, 598], [83, 52, 941, 531, 835, 169, 302, 430, 376, 954], [8587, 8094]),
    ([985, 939, 330, 130, 799, 133], [800, 500, 518, 226], [3855, 6533, 4213, 5775, 6848, 968]),
    ([104, 37, 100], [448, 289, 334, 907, 51, 515], [5393, 1722, 7663]),
    ([386, 308, 419, 578, 733, 6, 988, 487, 689, 703], [555, 312, 365, 851], [5002, 9900, 3669, 9369, 8183, 118, 2615, 2688, 1210]),
    ([653, 496, 37, 110, 700], [842, 994, 547], [2330, 3717, 9881, 5436]),
]

results = []
for startTime, endTime, profit in test_cases:
    result = solution.jobScheduling(startTime, endTime, profit)
    results.append(result)

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.jobScheduling(st, et, p) for st, et, p in test_cases]
)

for i, result in enumerate(results):
    print(f"Input: startTime={test_cases[i][0]}, endTime={test_cases[i][1]}, profit={test_cases[i][2]}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")