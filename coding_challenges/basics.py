import time


def three_sum(s):
    """ 3SUM problem asks if a given set of n real numbers contains three elements that sum to zero."""
    start = time.time()

    for i in s:
        for j in s:
            for k in s:
                if i + j + k == 0:
                    end = time.time()
                    return end-start



s = [-25, -10, -7, -3, 2, 4, 8, 10]


def string_builder(x):
    start = time.time()
    """An experiment, this is inefficient way to compose strings."""
    letter = '_cc_'
    letters = ''
    for i in range(x):
        letters += letter
    print time.time() - start


def better_string_builder(x):
    start = time.time()
    """An experiment, this is inefficient way to compose strings."""
    letter = '_cc_'
    letters = []
    for i in range(x):
        letters.append(letter)
    ''.join(letters)
    print time.time() -start


def check_perm(s1,s2):
    from itertools import permutations
    """ Check Permutation: Given two strings,
    write a method to decide if one is a permutation of the other. """

    if tuple(s2) in permutations(s1):
        print True


def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    start = time.time()
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    end = time.time()
    print end -start
    return string



n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def linear_sum(s,n):
    if n == 0:
        return 0
    else:
        return linear_sum(s, n-1) + s[n-1]


def binary_sum(s, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop: # zero elements in slice
        return 0
    elif start == stop - 1: # one element in slice
        return s[start]
    else: # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)

print binary_sum(arr,0,n)