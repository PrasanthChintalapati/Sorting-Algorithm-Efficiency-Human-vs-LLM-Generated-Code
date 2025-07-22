from collections import Counter, deque
from heapq import heapify, heappop, heappush
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
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return "".join(sorted(s))
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapify(heap)
        queue = deque()
        result = []
        while heap:
            count, char = heappop(heap)
            result.append(char)
            queue.append((count + 1, char))
            if len(queue) >= k:
                count, char = queue.popleft()
                if count < 0:
                    heappush(heap, (count, char))
        return "".join(result) if len(result) == len(s) else ""

solution = Solution()

test_cases = [
    ('cxruog', 2),
    ('mryxn', 1),
    ('zgysa', 2),
    ('xe', 2),
    ('fbqgxhr', 7),
    ('znvpkq', 5),
    ('pg', 2),
    ('jriqc', 4),
    ('vrnodhe', 4),
    ('xdiu', 3),
]

results = []
for s, k in test_cases:
    result = solution.rearrangeString(s, k)
    results.append((s, k, result))

execution_results, total_execution_time, peak_memory_usage = measure_execution(
    lambda: [solution.rearrangeString(s, k) for s, k in test_cases]
)

for (s, k, result) in results:
    print(f"Input: s='{s}', k={k}")
    print(f"Output: '{result}'")
    print("-" * 30)

print(f"Total Execution Time for all test cases: {total_execution_time:.6f} seconds")
print(f"Peak Memory Usage for all test cases: {peak_memory_usage:.6f} MB")