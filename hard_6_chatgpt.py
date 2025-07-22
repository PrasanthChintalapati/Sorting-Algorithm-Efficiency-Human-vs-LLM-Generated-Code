import time
import tracemalloc
from collections import defaultdict
from typing import List

# Start tracking memory and time
tracemalloc.start()
start_time = time.perf_counter()

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Create a dictionary to group positions by their values
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[mat[i][j]].append((i, j))
        
        # Arrays to track the maximum number of moves for each row and column
        rowMax = [0] * m
        colMax = [0] * n
        ans = 0
        
        # Process the matrix values sorted in ascending order
        for _, pos in sorted(g.items()):
            mx = []
            # Calculate the maximum path for each position in the current group
            for i, j in pos:
                mx.append(1 + max(rowMax[i], colMax[j]))
                ans = max(ans, mx[-1])
            # Update row and column maximums based on current positions
            for k, (i, j) in enumerate(pos):
                rowMax[i] = max(rowMax[i], mx[k])
                colMax[j] = max(colMax[j], mx[k])
        
        return ans

# Test cases inside the code
solution = Solution()

# Test case 1
assert solution.maxIncreasingCells([[-54427, 88451, 46633], [26731, -83107, -24124], [13958, -7969, -70806]]) == 4

# Test case 2
assert solution.maxIncreasingCells([[34506, -4479, 86403], [-26040, 56925, 7537]]) == 3

# Test case 3
assert solution.maxIncreasingCells([[-71835, -16974, 94617], [97053, -15912, 33374], [42792, 48002, -21800]]) == 5

# Test case 4
assert solution.maxIncreasingCells([[81312], [-95155], [-73698], [-52068], [98610]]) == 5

# Test case 5
assert solution.maxIncreasingCells([[89702], [-41759], [-10907], [-88197], [-49431]]) == 5

# Test case 6
assert solution.maxIncreasingCells([[94384, 54326, 44786], [76776, 66119, -87499], [-37833, 95265, -95706], [20752, 72903, 10283]]) == 8

# Test case 7
assert solution.maxIncreasingCells([[86274], [85560], [-71078]]) == 3

# Test case 8
assert solution.maxIncreasingCells([[-55178, 80097], [-33419, 95930]]) == 3

# Test case 9
assert solution.maxIncreasingCells([[2582, 8564, -84421, -98096], [71976, 64697, 79346, -81647], [33150, -85001, -69278, 1199], [10765, 51533, -82286, 52020]]) == 8

# Test case 10
assert solution.maxIncreasingCells([[-41870, 44279, -15637], [42526, 12842, 15470], [-2577, 54538, -1876], [90166, 9589, -22767]]) == 6

# Stop tracking time and memory
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)

# Print execution time and peak memory usage
print(f"Execution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")

# Stop tracking memory usage
tracemalloc.stop()
