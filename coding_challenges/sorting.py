from __future__ import print_function
from random import shuffle


def selection_sort(arr):
    n = len(arr)

    for i in xrange(n):
        mini = i
        j = i + 1
        print(arr[i])
        for k in xrange(j,n):
            if arr[k] < arr[mini]:
                mini = int(k)
        swap = arr[i]
        arr[i] = arr[mini]
        arr[mini] = swap


def insertion_sort_v2(arr):
    n = len(arr)
    counter = 0
    for i in range(1,n):
        for j in range(i, 0, -1):

            if arr[j] < arr[j-1]:

                counter = counter + 1

                swap = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = swap
            else:
                break
    print(counter)


def merge(S, S1, S2):

    i = j = 0

    while i+j < len(S):

        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]  # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i + j] = S2[j]  # copy jth element of S2 as next item of S
            j += 1


def merge_sort(arr):

    n = len(arr)
    if len(arr) < 2:
        return

    mid = len(arr)//2

    left = arr[0:mid]
    right = arr[mid:n]

    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)


class QuickSort(object):

    def __init__(self, arr):
        self.array = arr
        self.length = len(arr)

    def sort(self):
        self.__shuffle(self.array)
        self.__sort(self.array, 0, self.length - 1)

    @staticmethod
    def __shuffle(a):
        return shuffle(a)

    @staticmethod
    def __sort(a, lo, hi):
        if hi <= lo:
            return
        j = QuickSort.__partition(a, lo, hi)
        QuickSort.__sort(a, lo, j - 1)
        QuickSort.__sort(a, j + 1, hi)

    @staticmethod
    def __partition(a, lo, hi):

        i, j = lo + 1, hi

        while True:

            while a[i] < a[lo]:
                if i >= hi: break
                i += 1

            while a[j] > a[lo]:
                if j <= lo: break
                j -= 1

            if j <= i: break
            swap = a[i]
            a[i] = a[j]
            a[j] = swap

        swap = a[j]
        a[j] = a[lo]
        a[lo] = swap

        return j


a = [7, 10, 5, 3, 8, 4, 2, 9, 6]
l = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']




#SelectionSort(a)

# InsertionSort(a)
f = [5, 8, 1 ,3, 7, 9, 2]
QuickSort(l).sort()
print(l)

