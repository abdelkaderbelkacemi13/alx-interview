#!/usr/bin/python3
"""
A module to play Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of a Prime game.
    "x" is the rounds number.
    """
    if x < 1 or not nums:
        return None
    maria_rounds_win = 0
    ben_rounds_win = 0
    # generate prime numbers with a limit of the maximum number in nums
    n = max(nums)
    prime_numbers = [True for _ in range(1, n + 1, 1)]
    prime_numbers[0] = False
    for i, is_prime in enumerate(prime_numbers, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime_numbers[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, prime_numbers[0: n])))
        ben_rounds_win += primes_count % 2 == 0
        maria_rounds_win += primes_count % 2 == 1
    if maria_rounds_win == ben_rounds_win:
        return None
    return 'Maria' if maria_rounds_win > ben_rounds_win else 'Ben'
