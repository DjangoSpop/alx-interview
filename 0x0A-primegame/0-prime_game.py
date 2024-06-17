#!/usr/bin/python3
from typing import List
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_game(n):
    return 'Alice' if n % 2 == 0 else 'Bob' if is_prime(n) else 'Alice' 
    
def isWinner(x: int, nums: List[int]) -> str:
    alice_wins = 0
    bob_wins = 0
    for n in nums:
        if prime_game(n) == 'Alice':
            alice_wins += 1
        else:
            bob_wins += 1
    if alice_wins > bob_wins:
        return 'Alice'
    elif bob_wins > alice_wins:
        return 'Bob'
    else:
        return None
        pass
        