def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def memoize(func):
        cache = {}

        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return wrapper

    @memoize
    def play_game(n):
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
