from typing import List
import heapq
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
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        t = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        ans = tot = 0
        mod = 10**9 + 7
        h = []
        for s, e in t:
            tot += s
            ans = max(ans, tot * e)
            heapq.heappush(h, s)
            if len(h) == k:
                tot -= heapq.heappop(h)
        return ans % mod

solution = Solution()
test_cases = [
    (8, [34679, 64913, 91615, 36507, 5692, 79863, 12106, 83279], [55530105, 16236480, 5381995, 69521335, 37788889, 35198827, 97603826, 20795853], 4),
    (8, [33997, 58192, 43110, 81875, 64251, 25273, 25183, 9631], [12378277, 73396563, 58739455, 25200880, 36629527, 67049554, 71417242, 56664327], 7),
    (3, [92695, 35393, 84682], [62265131, 94139466, 14861492], 1),
    (4, [31908, 91768, 37269, 17515], [97154430, 94173877, 72068014, 41800465], 2),
    (7, [68710, 45893, 55238, 43288, 84537, 12541, 47430], [35932623, 91639628, 54106761, 3205074, 90538613, 47158848, 94087846], 2),
    (8, [52308, 56278, 61841, 59469, 95567, 67644, 41799, 34575], [40971606, 78826087, 53028153, 15241601, 94808174, 30791448, 11987897, 22942585], 2),
    (10, [53763, 65040, 99168, 41476, 603, 47750, 9325, 55783, 67889, 87438], [18802955, 98710493, 89863138, 7633041, 58114719, 6515359, 73579299, 29121300, 59308383, 46772256], 5),
    (6, [1908, 57473, 83114, 65103, 16232, 32152], [21460512, 15635077, 5469392, 13806096, 14507704, 44660137], 6),
    (9, [77159, 58479, 4772, 16318, 75644, 14573, 2586, 19917, 61477], [53397244, 72622505, 69717224, 60683451, 62320452, 53323790, 81600885, 45784977, 30601609], 9),
    (8, [3879, 54156, 1804, 21603, 96931, 40742, 38347, 26556], [3608484, 70236817, 84528592, 38415404, 40811038, 90809484, 13960265, 14544398], 8),
]

results = []
for n, speed, efficiency, k in test_cases:
    result = solution.maxPerformance(n, speed, efficiency, k)
    results.append(result)

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.maxPerformance(n, speed, efficiency, k) for n, speed, efficiency, k in test_cases]
)

for i, result in enumerate(results):
    n, speed, efficiency, k = test_cases[i]
    print(f"Input: n={n}, speed={speed}, efficiency={efficiency}, k={k}")
    print(f"Output: {result}")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")