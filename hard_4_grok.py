
from typing import List
from bisect import bisect_right

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        mod = 10**9 + 7
        packages.sort()
        n = len(packages)
        total_package_size = sum(packages)
        min_waste = float('inf')
        
        for box_sizes in boxes:
            box_sizes.sort()
            if box_sizes[-1] < packages[-1]:
                continue  # Largest box too small for largest package
            
            total_box_size = 0
            prev_idx = 0
            for box_size in box_sizes:
                # Find how many packages can fit in this box size
                curr_idx = bisect_right(packages, box_size, lo=prev_idx)
                total_box_size += (curr_idx - prev_idx) * box_size
                prev_idx = curr_idx
                if prev_idx == n:
                    break  # All packages assigned
            
            if prev_idx == n:  # All packages must be assigned
                min_waste = min(min_waste, total_box_size - total_package_size)
        
        return min_waste % mod if min_waste != float('inf') else -1

# Full code to save as min_wasted_space.py
import time
import tracemalloc
from typing import List
from bisect import bisect_right

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        mod = 10**9 + 7
        packages.sort()
        n = len(packages)
        total_package_size = sum(packages)
        min_waste = float('inf')
        
        for box_sizes in boxes:
            box_sizes.sort()
            if box_sizes[-1] < packages[-1]:
                continue  # Largest box too small for largest package
            
            total_box_size = 0
            prev_idx = 0
            for box_size in box_sizes:
                # Find how many packages can fit in this box size
                curr_idx = bisect_right(packages, box_size, lo=prev_idx)
                total_box_size += (curr_idx - prev_idx) * box_size
                prev_idx = curr_idx
                if prev_idx == n:
                    break  # All packages assigned
            
            if prev_idx == n:  # All packages must be assigned
                min_waste = min(min_waste, total_box_size - total_package_size)
        
        return min_waste % mod if min_waste != float('inf') else -1

# Test cases execution
if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.perf_counter()
    
    solution = Solution()
    test_cases = [
        ([2,3,5], [[4,8],[2,8]], 6),
        ([2,3,5], [[1,4],[2,3],[3,4]], -1),
        ([3,5,8,10,11,12], [[12],[11,9],[10,5,14]], 9),
        ([18,46,82,84,95,100], [[54,58],[8,11,20,44,49,62,72,79,88,95],[5,47,54,57,68,75,91,94,100],[41,77],[11,59],[1,17,30,43,46,55,60,70,79,88]], 51),
        ([5,12,20,22,34,42,57,80,86], [[58,93,97],[26,50,77,94],[8,14,18,48,53,56,65,71,97],[14,27,41,66,93],[3,6,15,21,40,52,59,76,78,89],[7,22,31,37,62,73],[11,25,40,47,55,59,76,83,91]], 48),
        ([36,75], [[42],[8,14,19,25,33,43,70,72,81,88],[13,22,31,32,44,49,52,95],[48,64],[2,6,11,23,55,57,74,75,92,93],[51,76],[24]], 13),
        ([41,43,55,95], [[13,15,51,99],[3,8,16,58,67,74,77,91,99],[21,26,37,50],[54,94],[29,39,49,55,58,74,79,96],[13,37,45,59,66,79,88,94],[8,22,23,56,81,83]], 15),
        ([19,25,82], [[30,45,60],[8,9,29,34,63,84,91,95,100],[47,56,95],[15,25,65,67,85,86,87]], 9),
        ([26,35,87], [[55,81,94],[21,31,32,69,77,96]], 48),
        ([46,61,83], [[9,18,35,36,64,74,94,98],[25,33,38,53,66,72,84],[58,99],[50]], 13),
        ([11,13,45,50,67,80,96], [[10,12,17,21,24,63,81,82]], -1),
        ([24,47,49,65,72,77,85], [[23,57,82],[15,16,34,40,43,61,94],[40],[3,14,24,25,43,92,95,100],[3],[13,20,24,31,50,61,66,82],[4,6,20,44,68,83,89],[73],[20,35,53,56,76],[10,22,30,84]], 84),
        ([10,69,70], [[3,17,18,24,46,47,65,71,77,80],[12,67],[45,69,70,95],[3,21,27,33,50,53,56,71,86],[6,90],[3,4,19,20,22,27,46,83,85,99],[5,6,20,44,70,85,92,99],[11,22,31,38,43,49,56,66,68],[5,7,46,76,86,88,95]], 10)
    ]
    
    for i, (packages, boxes, expected) in enumerate(test_cases, 1):
        result = solution.minWastedSpace(packages, boxes)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: packages={packages}, boxes={boxes}, output={result}")
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    execution_time_s = end_time - start_time
    peak_memory_mb = peak / (1024 * 1024)
    print(f"\nExecution Time: {execution_time_s:.6f} seconds")
    print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
    tracemalloc.stop()