"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other"""

"""
SOLUTION
Like in many questions, we should confirm some details with our interviewer. We should understand if the
permutation comparison is case sensitive. That is: is God a permutation of dog? Additionally, we should
ask if whitespace is significant. We will assume for this problem that the comparison is case sensitive and
whitespace is significant. So, "god
" is different from "dog".
Observe first that strings of different lengths cannot be permutations of each other. There are two easy
ways to solve this problem, both of which use this optimization.

Solution #1: Sort the strings.
If two strings are permutations, then we know they have the same characters, but in different orders. There­
fore, sorting the strings will put the characters from two permutations in the same order. We just need to
compare the sorted versions of the strings.
"""
from collections import Counter
def is_permutation_sorted(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    
    return sorted(string_a) == sorted(string_b)

# print(is_permutation_sorted('god','dog'))


"""
Solution #2: Check if the two strings have identical character counts.
"""

def is_permutation_count(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    return Counter(string_a) == Counter(string_b)
print(is_permutation_count('god',' dog'))
