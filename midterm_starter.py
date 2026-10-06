import time
import random

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    Fairly compare the two duplicate-detection algorithms across several input sizes.
    This benchmarking setup isolates the algorithms themselves rather than timing data
    generation or random variation.
    """
    sizes = [100, 200, 500, 1000, 2000, 5000]
    trials = 5
    rng = random.Random(42)

    print(f"{'n':>8} {'slow avg (s)':>14} {'fast avg (s)':>14} {'ratio':>10}")
    print("-" * 52)

    for n in sizes:
        data = rng.sample(range(2 * n), n)

        slow_times = []
        fast_times = []

        for _ in range(trials):
            start = time.perf_counter()
            find_duplicates_slow(data)
            slow_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            find_duplicates_fast(data)
            fast_times.append(time.perf_counter() - start)

        slow_avg = sum(slow_times) / len(slow_times)
        fast_avg = sum(fast_times) / len(fast_times)
        ratio = float("inf") if fast_avg == 0 else slow_avg / fast_avg

        print(f"{n:>8} {slow_avg:>14.8f} {fast_avg:>14.8f} {ratio:>10.2f}x")


if __name__ == "__main__":
    flawed_benchmark()