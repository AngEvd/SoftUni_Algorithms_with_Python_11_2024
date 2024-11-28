def simulate_loops(n, depth=1, current=None):
    if current is None:
        current = []
    if depth > n:
        return [current]
    results = []
    for i in range(1, n + 1):
        results.extend(simulate_loops(n, depth + 1, current + [i]))
    return results


for item in simulate_loops(int(input())):
    print(" ".join(map(str, item)))
