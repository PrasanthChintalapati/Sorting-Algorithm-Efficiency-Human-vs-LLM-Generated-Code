from typing import List
from collections import defaultdict
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
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[mat[i][j]].append((i, j))
        rowMax = [0] * m
        colMax = [0] * n
        ans = 0
        for _, pos in sorted(g.items()):
            mx = []
            for i, j in pos:
                mx.append(1 + max(rowMax[i], colMax[j]))
                ans = max(ans, mx[-1])
            for k, (i, j) in enumerate(pos):
                rowMax[i] = max(rowMax[i], mx[k])
                colMax[j] = max(colMax[j], mx[k])
        return ans

solution = Solution()
test_cases = [
    ([[-54427, 88451, 46633], [26731, -83107, -24124], [13958, -7969, -70806]]),
    ([[-71835, -16974, 94617], [97053, -15912, 33374], [42792, 48002, -21800]]),
    ([[81312], [-95155], [-73698], [-52068], [98610]]),
    ([[89702], [-41759], [-10907], [-88197], [-49431]]),
    ([[94384, 54326, 44786], [76776, 66119, -87499], [-37833, 95265, -95706], [20752, 72903, 10283]]),
    ([[86274], [85560], [-71078]]),
    ([[-55178, 80097], [-33419, 95930]]),
    ([[2582, 8564, -84421, -98096], [71976, 64697, 79346, -81647], [33150, -85001, -69278, 1199], [10765, 51533, -82286, 52020]]),
    ([[-41870, 44279, -15637], [42526, 12842, 15470], [-2577, 54538, -1876], [90166, 9589, -22767]]),
    ([[34506, -4479, 86403], [-26040, 56925, 7537]]),
]

results = []
for mat in test_cases:
    result = solution.maxIncreasingCells(mat)
    results.append(result)

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.maxIncreasingCells(m) for m in test_cases]
)

for i, result in enumerate(results):
    print(f"Input: mat={test_cases[i]}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")