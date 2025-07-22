import time
import tracemalloc
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s  # No rearrangement needed if k == 0
        if k == 1:
            return ''.join(sorted(s))  # Return sorted string for k == 1
        
        # Count frequency of each character
        freq = Counter(s)
        
        # Check if rearrangement is possible
        max_freq = max(freq.values())
        if max_freq > (len(s) + k - 1) // k:
            return ""  # Too many occurrences of a character
        
        # Create max heap of (negated frequency, character)
        heap = [(-count, char) for char, count in freq.items()]
        heapify(heap)
        
        result = []
        blocked = deque()  # To enforce k distance
        
        while heap or blocked:
            # Release characters from blocked queue if k positions have passed
            if len(result) >= k and blocked:
                freq, char = blocked.popleft()
                if freq > 0:
                    heappush(heap, (-freq, char))
            
            if not heap:
                return ""  # Cannot place remaining characters
            
            # Get the most frequent character
            count, char = heappop(heap)
            count = -count  # Convert back to positive
            result.append(char)
            
            # Block this character for k positions
            if count > 1:
                blocked.append((count - 1, char))
        
        # Verify the result length
        if len(result) != len(s):
            return ""
        
        # Verify k distance constraint
        for i in range(len(result) - k + 1):
            for j in range(i + 1, i + k):
                if j < len(result) and result[i] == result[j]:
                    return ""  # Same characters too close
        
        return "".join(result)

# Test cases execution
if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.perf_counter()
    
    solution = Solution()
    test_cases = [
        ("aabbcc", 3, "abcabc"),
        ("aaabc", 3, ""),
        ("aaadbbcc", 2, "abacabcd"),
        ("cxruog", 2, "cgorux"),
        ("mryxn", 1, "mnrxy"),
        ("zgysa", 2, "agsyz"),
        ("xe", 2, "ex"),
        ("fbqgxhr", 7, "bfghqrx"),
        ("znvpkq", 5, "knpqvz"),
        ("pg", 2, "gp"),
        ("jriqc", 4, "cijqr"),
        ("vrnodhe", 4, "dehnorv"),
        ("xdiu", 3, "diux")
    ]
    
    for i, (s, k, expected) in enumerate(test_cases, 1):
        result = solution.rearrangeString(s, k)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: s={s}, k={k}, output={result}")
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    execution_time_s = end_time - start_time
    peak_memory_mb = peak / (1024 * 1024)
    print(f"\nExecution Time: {execution_time_s:.6f} seconds")
    print(f"Peak Memory Usage: {peak_memory_mb:.6f} MB")
    tracemalloc.stop()