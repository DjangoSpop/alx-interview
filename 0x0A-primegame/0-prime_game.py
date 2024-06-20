#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: Name of the player that won the most rounds.
         If the winner cannot be determined, return None.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Use Sieve of Eratosthenes to precompute primes
    sieve = [True for _ in range(max(max_num + 1, 2))]
    sieve[0] = sieve[1] = False
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    # Count primes for each number
    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i-1]
        if sieve[i]:
            prime_counts[i] += 1

    maria_wins = sum(prime_counts[n] % 2 == 1 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
