#!/usr/bin/python3
def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        nums = set(range(1, n + 1))
        player = 0
        while True:
            found_prime = False
            for num in nums:
                if is_prime(num):
                    found_prime = True
                    nums.remove(num)
                    for multiple in range(num * 2, n + 1, num):
                        nums.discard(multiple)
                    break
            if not found_prime:
                return player
            player = 1 - player

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
