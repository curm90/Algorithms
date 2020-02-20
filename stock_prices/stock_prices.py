#!/usr/bin/python

import argparse


def find_max_profit(prices):
    ''' Returns the max profit to be made from single buy, sell'''

    # a place to store profit
    max_profit = prices[1] - prices[0]
    # place to store min price
    min_price = prices[0]
    # loop over prices
    for i in range(1, len(prices)):
        # if prices[i] - min_price > max_profit
        if prices[i] - min_price > max_profit:
            # set max profit = to current price - current min price
            max_profit = prices[i] - min_price
          # if prices[i] < current min price
        if prices[i] < min_price:
            # set min price to prices[i]
            min_price = prices[i]

    return max_profit

    # one liner solution
    # return max(prices[1:]) - min(prices[:prices.index(max(prices[1:]))])


# find_max_profit([10, 7, 5, 8, 11, 9])
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
