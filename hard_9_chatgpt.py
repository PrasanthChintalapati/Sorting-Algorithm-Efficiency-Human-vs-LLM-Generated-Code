import time
import tracemalloc

# Start memory tracking
tracemalloc.start()
start_time = time.perf_counter()

class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        # Sort the tasks based on their end time
        tasks.sort(key=lambda x: x[1])
        
        # Initialize the visited time slots array
        vis = [0] * 2010  # 2010 slots to handle time range up to 2000
        
        ans = 0  # Total time the computer is turned on
        
        # Process each task
        for start, end, duration in tasks:
            # Calculate remaining duration to be completed
            duration -= sum(vis[start : end + 1])
            
            # Try to fill the time slots from end to start
            i = end
            while i >= start and duration > 0:
                if not vis[i]:  # If the slot is not already used
                    duration -= 1
                    vis[i] = 1  # Mark the slot as used
                    ans += 1  # Increment the total time
                i -= 1  # Move to the previous time slot
        
        return ans

# End time tracking
end_time = time.perf_counter()

# Calculate memory usage and execution time
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)
print(f"Execution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")

# Stop memory tracking
tracemalloc.stop()

# Test cases
solution = Solution()

# Test case 1
assert solution.findMinimumTime([[3, 7, 5], [3, 7, 1], [4, 10, 5], [10, 10, 1]]) == 6

# Test case 2
assert solution.findMinimumTime([[4, 5, 2], [5, 7, 3], [6, 7, 2], [9, 9, 1], [8, 10, 3]]) == 7

# Test case 3
assert solution.findMinimumTime([[1, 1, 1], [6, 7, 2], [1, 7, 7], [7, 9, 1], [7, 9, 3], [7, 10, 3], [10, 10, 1], [9, 10, 2], [1, 10, 5], [10, 10, 1]]) == 10

# Test case 4
assert solution.findMinimumTime([[3, 4, 2], [3, 5, 1], [1, 5, 4], [5, 5, 1], [5, 7, 3], [1, 7, 4], [1, 8, 7], [7, 8, 1], [5, 10, 1], [10, 10, 1]]) == 8

# Test case 5
assert solution.findMinimumTime([[1, 3, 2], [8, 8, 1], [3, 9, 5], [8, 10, 1]]) == 6

# Test case 6
assert solution.findMinimumTime([[2, 3, 1], [7, 8, 2], [8, 8, 1]]) == 3

# Test case 7
assert solution.findMinimumTime([[2, 8, 1], [7, 8, 1]]) == 1

# Test case 8
assert solution.findMinimumTime([[5, 7, 2], [9, 9, 1], [10, 10, 1]]) == 4

# Test case 9
assert solution.findMinimumTime([[2, 6, 1], [5, 7, 2], [10, 10, 1]]) == 3

# Test case 10
assert solution.findMinimumTime([[2, 2, 1], [6, 7, 1], [3, 8, 2], [4, 9, 2], [9, 9, 1], [4, 10, 5], [10, 10, 1], [10, 10, 1]]) == 6
