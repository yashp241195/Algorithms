# Making change

coin = [10, 6, 1]
exchange = []


def make_change(c, exchange):
    if c == 0:
        print(exchange," len = ", len(exchange))
        return 0
    else:
        min_coins = c + 1
        for i in range(len(coin)):
            if c - coin[i] >= 0:
                exchange.append(coin[i])
                make_change(c - coin[i], exchange)
                exchange.pop(len(exchange)-1)

        return min_coins + 1


make_change(12, exchange)
