# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False  # found duplicate pair
    return True  # if we reach this, elements were unique


def check_duplicates(s):
    """Return duplicates elements in sequence s."""
    dup = []
    temp = sorted(s)  # create a sorted copy of S
    for j in range(1, len(temp)):
        if s[j - 1] == s[j]:
            dup.append(s[j])

    if dup:
        return dup
    return False


import unittest


class TestUniqueness(unittest.TestCase):
    ulist = [1, 2, 3, 5]
    dlist = [1, 2, 3, 5, 5, 7, 7, 9]

    def test_is_unique(self):
        self.assertTrue(check_duplicates(TestUniqueness.dlist))

    def test_duplication(self):

        duplicated_element = check_duplicates(TestUniqueness.dlist)
        self.assertEqual([5, 7], duplicated_element)


if __name__ == '__main__':

    a = [1, 2, 3,  5, 5, 7, 7, 9]
    print check_duplicates(a)
    unittest.main()
