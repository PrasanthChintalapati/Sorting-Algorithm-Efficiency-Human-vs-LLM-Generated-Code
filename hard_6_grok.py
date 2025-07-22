from collections import defaultdict
from typing import List
import time
import tracemalloc

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # Group cells by value
        value_to_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_cells[mat[i][j]].append((i, j))
        
        # Track maximum path length ending at each row and column
        row_max = [0] * m
        col_max = [0] * n
        max_path = 0
        
        # Process cells in ascending order of values
        for value in sorted(value_to_cells.keys()):
            # Compute max path for each cell with current value
            curr_max = []
            for i, j in value_to_cells[value]:
                # Max path is 1 plus the maximum from same row or column
                path_len = 1 + max(row_max[i], col_max[j])
                curr_max.append(path_len)
                max_path = max(max_path, path_len)
            
            # Update row_max and col_max for next iteration
            for k, (i, j) in enumerate(value_to_cells[value]):
                row_max[i] = max(row_max[i], curr_max[k])
                col_max[j] = max(col_max[j], curr_max[k])
        
        return max_path

# Run test cases with timing and memory tracking
tracemalloc.start()
start_time = time.perf_counter()

solution = Solution()

# Test cases
test_cases = [
    ([[-54427, 88451, 46633], [26731, -83107, -24124], [13958, -7969, -70806]], 4),
    ([[34506, -4479, 86403], [-26040, 56925, 7537]], 3),
    ([[-71835, -16974, 94617], [97053, -15912, 33374], [42792, 48002, -21800]], 5),
    ([[81312], [-95155], [-73698], [-52068], [98610]], 5),
    ([[89702], [-41759], [-10907], [-88197], [-49431]], 5),
    ([[94384, 54326, 44786], [76776, 66119, -87499], [-37833, 95265, -95706], [20752, 72903, 10283]], 8),
    ([[86274], [85560], [-71078]], 3),
    ([[-55178, 80097], [-33419, 95930]], 3),
    ([[2582, 8564, -84421, -98096], [71976, 64697, 79346, -81647], [33150, -85001, -69278, 1199], [10765, 51533, -82286, 52020]], 8),
    ([[-41870, 44279, -15637], [42526, 12842, 15470], [-2577, 54538, -1876], [90166, 9589, -22767]], 6)
]

for i, (mat, expected) in enumerate(test_cases, 1):
    result = solution.maxIncreasingCells(mat)
    assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print(f"Test case {i} passed: Input {mat}, Output {result}")

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)

print(f"\nExecution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
tracemalloc.stop()