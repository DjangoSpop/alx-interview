#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers  stones in each round.

    Returns:
        str: The name of the winner ("Maria" or "Ben") or None if it's a tie.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def memoize(func):
        """
        A decorator function that memoizes the result of a function call.

        Args:
            func (function): The function to be memoized.

        Returns:
            function: The memoized version of the function.
        """
        cache = {}

        def wrapper(n):
            """
            A wrapper function that caches the result.

            Args:
                n (int): The input value for the decorated function.

            Returns:
                The result of the decorated function for the given input value.
            """
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return wrapper

    @memoize
    def play_game(n):
        """
        Determines if a player can win the prime game.

        Args:
            n (int): The number of stones.

        Returns:
            bool: True if the player can win the game, False otherwise.
        """
        if n == 1:
            return False
        for i in range(2, n + 1):
            if is_prime(i) and not play_game(n - i):
                return True
        return False

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
