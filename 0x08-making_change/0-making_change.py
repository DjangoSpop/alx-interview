#!/usr/bin/python3
"""Change making module."""


def makeChange(coins, total):
    """_summary.

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if total <= 0:
        return 0

    # Create an array to store the minimum number
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins required for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins required to reach the total value
    return min_coins[total] if min_coins[total] != float('inf') else -1
