import time
import tracemalloc
from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return ''.join(sorted(s))  # If k==0, any arrangement is fine, sorted for consistency

        h = [(-v, c) for c, v in Counter(s).items()]
        heapify(h)
        q = deque()
        ans = []
        
        while h:
            v, c = heappop(h)
            ans.append(c)
            v = -v - 1
            q.append((v, c))
            
            if len(q) >= k:
                w, ch = q.popleft()
                if w > 0:
                    heappush(h, (-w, ch))
        
        return "".join(ans) if len(ans) == len(s) else ""

# Start timing and memory tracking
tracemalloc.start()
start_time = time.perf_counter()

# Provided test cases
solution = Solution()
assert solution.rearrangeString('cxruog', 2) == 'cgorux'
assert solution.rearrangeString('mryxn', 1) == 'mnrxy'
assert solution.rearrangeString('zgysa', 2) == 'agsyz'
assert solution.rearrangeString('xe', 2) == 'ex'
assert solution.rearrangeString('fbqgxhr', 7) == 'bfghqrx'
assert solution.rearrangeString('znvpkq', 5) == 'knpqvz'
assert solution.rearrangeString('pg', 2) == 'gp'
assert solution.rearrangeString('jriqc', 4) == 'cijqr'
assert solution.rearrangeString('vrnodhe', 4) == 'dehnorv'
assert solution.rearrangeString('xdiu', 3) == 'diux'

# Stop timing and memory tracking
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Output
execution_time_s = end_time - start_time
peak_memory_mb = peak / (1024 * 1024)
print("All test cases passed.")
print(f"Execution Time: {execution_time_s:.6f} seconds")
print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
