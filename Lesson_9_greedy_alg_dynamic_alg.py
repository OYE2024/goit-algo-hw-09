def find_coins_greedy(rest):
    coints = [50, 25, 10, 5, 2, 1]
    coints_counter = {}
    for i in coints:
        coints_counter[i] = 0
    for coin in coints:
        while rest >= coin:
            rest -= coin
            coints_counter[coin] += 1
    return {coin: count for coin, count in coints_counter.items() if count > 0}


rest = 120
print(find_coins_greedy(rest))
