#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    '''Returns all possbile plays of rps given inout n '''

    # a place to store the plays
    rps = ['rock', 'paper', 'scissors']
    # a place to store the result
    result = []

    # define an inner recursive helper funtion
    def recusive_helper(arr, n):
        # base case if n is 0 return initial rps list
        if n == 0:
            return result.append(arr)
        # else, loop over rps, feed arr to helper function
        # and append all plays to result arr
        for play in rps:
            recusive_helper(arr + [play], n-1)

    # initial call to kick off recursion
    recusive_helper([], n)
    return result


print(rock_paper_scissors(4))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
