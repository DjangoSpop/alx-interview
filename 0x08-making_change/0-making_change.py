#!/usr/bin/python3
"""Change making module using BFS."""

from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): A list of the values of the coins in possession.
                      Each coin value is an integer greater than 0.
        total (int): The target amount to meet.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize a queue to hold the current amount and.
    queue = deque([(0, 0)])  # (current amount, number of coins used)
    visited = set()  # To keep track of visited amounts

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin
            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1  # If we exhaust the queue without finding the total
