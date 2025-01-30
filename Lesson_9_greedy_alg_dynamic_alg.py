def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coins_counter = {}
    for i in coins:
        coins_counter[i] = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coins_counter[coin] += 1
    return {coin: count for coin, count in coins_counter.items() if count > 0}


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    hash = {}

    def dp(remaining):
        if remaining == 0:
            return {}
        if remaining < 0:
            return None
        if remaining in hash:
            return hash[remaining]

        best_solution = None
        for coin in coins:
            sub_solution = dp(remaining - coin)
            if sub_solution is not None:
                new_solution = sub_solution.copy()
                new_solution[coin] = new_solution.get(coin, 0) + 1
                if best_solution is None or sum(new_solution.values()) < sum(best_solution.values()):
                    best_solution = new_solution

        hash[remaining] = best_solution
        return best_solution

    result = dp(amount)
    return result if result is not None else {}


amount = 127950
print(find_coins_greedy(amount))
print(find_min_coins(amount))
