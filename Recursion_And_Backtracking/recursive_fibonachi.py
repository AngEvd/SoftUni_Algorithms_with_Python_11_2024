def recursive_fibonachi(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1

    memo[n] = recursive_fibonachi(n - 1, memo) + recursive_fibonachi(n - 2, memo)
    return memo[n]


print(recursive_fibonachi(int(input())))