import time
import tracemalloc
from bisect import bisect_right
from typing import List

# Start memory tracking and timer
tracemalloc.start()
start_time = time.perf_counter()

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the jobs into a list of tuples and sort by end time
        jobs = sorted(zip(endTime, startTime, profit))
        
        # Initialize dp array where dp[i] will store the maximum profit up to job i
        n = len(profit)
        dp = [0] * (n + 1)
        
        # Iterate through all jobs
        for i, (_, s, p) in enumerate(jobs):
            # Find the index of the last non-conflicting job using binary search
            j = bisect_right(jobs, s, hi=i, key=lambda x: x[0])
            
            # Update dp[i+1] by considering whether to take this job or not
            dp[i + 1] = max(dp[i], dp[j] + p)
        
        # The last value in dp is the maximum profit we can obtain
        return dp[n]

# Test case
solution = Solution()

# Test Case 1
assert solution.jobScheduling([788, 846, 685, 926, 120, 892, 426, 144, 67, 885], 
                              [376, 218, 161, 774, 474], 
                              [7594, 3954, 6603, 4847, 1229]) == 22998

# Test Case 2
assert solution.jobScheduling([614, 238, 89], 
                              [28, 776, 834, 124, 439], 
                              [9203, 5748, 1333, 4358, 5075, 7922, 7958]) == 0

# Test Case 3
assert solution.jobScheduling([358, 742, 446, 70], 
                              [921, 546, 793], 
                              [9103, 2328, 1233, 55, 8593, 9166, 2855]) == 0

# Test Case 4
assert solution.jobScheduling([32, 989, 188, 863, 117], 
                              [807, 271, 229, 920, 225, 446], 
                              [613, 5471, 3971, 8692, 6863, 2314, 3201, 4057, 1207, 7937]) == 0

# Test Case 5
assert solution.jobScheduling([667, 941, 125, 840], 
                              [268, 545], 
                              [4882, 5023, 3029, 2727, 5899, 757]) == 0

# Test Case 6
assert solution.jobScheduling([899, 613, 598], 
                              [83, 52, 941, 531, 835, 169, 302, 430, 376, 954], 
                              [8587, 8094]) == 16681

# Test Case 7
assert solution.jobScheduling([985, 939, 330, 130, 799, 133], 
                              [800, 500, 518, 226], 
                              [3855, 6533, 4213, 5775, 6848, 968]) == 0

# Test Case 8
assert solution.jobScheduling([104, 37, 100], 
                              [448, 289, 334, 907, 51, 515], 
                              [5393, 1722, 7663]) == 7663

# Test Case 9
assert solution.jobScheduling([386, 308, 419, 578, 733, 6, 988, 487, 689, 703], 
                              [555, 312, 365, 851], 
                              [5002, 9900, 3669, 9369, 8183, 118, 2615, 2688, 1210]) == 0

# Test Case 10
assert solution.jobScheduling([653, 496, 37, 110, 700], 
                              [842, 994, 547], 
                              [2330, 3717, 9881, 5436]) == 0

# End memory tracking and timer
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)

# Print execution time and peak memory usage
print(f"Execution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")

# Stop memory tracking
tracemalloc.stop()
