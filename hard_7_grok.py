from typing import List
from heapq import heappush, heappop
import time
import tracemalloc

# Solution class (same as above)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        total_speed = 0
        max_perf = 0
        speed_heap = []
        mod = 10**9 + 7
        
        for eff, spd in engineers:
            heappush(speed_heap, spd)
            total_speed += spd
            if len(speed_heap) > k:
                total_speed -= heappop(speed_heap)
            max_perf = max(max_perf, total_speed * eff)
        
        return max_perf % mod

# Start memory and time tracking
tracemalloc.start()
start_time = time.perf_counter()

# Initialize solution
solution = Solution()

# Test cases
test_cases = [
    (
        8,
        [34679, 64913, 91615, 36507, 5692, 79863, 12106, 83279],
        [55530105, 16236480, 5381995, 69521335, 37788889, 35198827, 97603826, 20795853],
        4,
        864578991
    ),
    (
        8,
        [33997, 58192, 43110, 81875, 64251, 25273, 25183, 9631],
        [12378277, 73396563, 58739455, 25200880, 36629527, 67049554, 71417242, 56664327],
        7,
        999006195
    ),
    (
        3,
        [92695, 35393, 84682],
        [62265131, 94139466, 14861492],
        1,
        666277648
    ),
    (
        4,
        [31908, 91768, 37269, 17515],
        [97154430, 94173877, 72068014, 41800465],
        2,
        48330323
    ),
    (
        7,
        [68710, 45893, 55238, 43288, 84537, 12541, 47430],
        [35932623, 91639628, 54106761, 3205074, 90538613, 47158848, 94087846],
        2,
        109058135
    ),
    (
        8,
        [52308, 56278, 61841, 59469, 95567, 67644, 41799, 34575],
        [40971606, 78826087, 53028153, 15241601, 94808174, 30791448, 11987897, 22942585],
        2,
        347096732
    ),
    (
        10,
        [53763, 65040, 99168, 41476, 603, 47750, 9325, 55783, 67889, 87438],
        [18802955, 98710493, 89863138, 7633041, 58114719, 6515359, 73579299, 29121300, 59308383, 46772256],
        5,
        524000493
    ),
    (
        6,
        [1908, 57473, 83114, 65103, 16232, 32152],
        [21460512, 15635077, 5469392, 13806096, 14507704, 44660137],
        6,
        632186626
    ),
    (
        9,
        [77159, 58479, 4772, 16318, 75644, 14573, 2586, 19917, 61477],
        [53397244, 72622505, 69717224, 60683451, 62320452, 53323790, 81600885, 45784977, 30601609],
        9,
        938549355
    ),
    (
        8,
        [3879, 54156, 1804, 21603, 96931, 40742, 38347, 26556],
        [3608484, 70236817, 84528592, 38415404, 40811038, 90809484, 13960265, 14544398],
        8,
        377837468
    )
]

# Run test cases
for i, (n, speed, efficiency, k, expected) in enumerate(test_cases, 1):
    result = solution.maxPerformance(n, speed, efficiency, k)
    assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print(f"Test case {i} passed: n={n}, k={k}, Output={result}")

# Calculate and print execution time and memory usage
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)

print(f"\nExecution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
tracemalloc.stop()