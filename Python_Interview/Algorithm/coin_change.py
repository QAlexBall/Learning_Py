def coin_change(values, values_counts, money, coins_used):
    for cents in range(1, money + 1):
        min_coins = cents
        for kind in range(0, values_counts):
            if values[kind] <= cents:
                temp = coins_used[cents - values[kind]] + 1
                if temp < min_coins:
                    min_coins = temp
        coins_used[cents] = min_coins
        print('{0}: {1}'.format(cents, coins_used[cents]))