""""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

SOLUTION
There is a "brute force" algorithm to do this. We could check all possible strings that are one edit away by
testing the removal of each character (and comparing), testing the replacement of each character (and
comparing), and then testing the insertion of each possible character (and comparing).
That would be too slow, so let's not bother with implementing it.
This is one of those problems where it's helpful to think about the "meaning" of each of these operations.
What does it mean for two strings to be one insertion, replacement, or removal away from each other?
Replacement: Consider two strings, such as bale and pale, that are one replacement away. Yes, that
does mean that you could replace a character in bale to make pale. But more precisely, it means that
they are different only in one place.
•
Insertion: The strings apple and aple are one insertion away. This means that if you compared the
strings, they would be identical-except for a shift at some point in the strings.
•
Removal: The strings apple and aple are also one removal away, since removal is just the inverse of
insertion.
We can go ahead and implement this algorithm now. We'll merge the insertion and removal check into one
step, and check the replacement step separately.
Observe that you don't need to check the strings for insertion, removal, and replacement edits. The lengths
of the strings will indicate which of these you need to check.
"""

# solution 1
def one_edit_away(string_a, string_b):
    str_a_len = len(string_a)
    str_b_len = len(string_b)

    if str_a_len == str_b_len:
        return one_edit_replace(string_a, string_b)
    elif str_a_len - 1 == str_b_len:
        return one_edit_insert(string_a, string_b)
    elif str_a_len + 1 == str_b_len:
        return one_edit_insert(string_a, string_b)
    return False


def one_edit_replace(string_a, string_b):
    difference_flag = False
    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            if difference_flag:
                return False
            difference_flag = True
    return True


# Check if you can insert a character into string_a to make string_2.
def one_edit_insert(string_a, string_b):
    index_1,index_2 = 0, 0
    while index_1 < len(string_a) and index_2 < len(string_b):
        if string_a[index_1] != string_b[index_2]:
            if index_1 != index_2:
                return False
            index_2+=1
        else:
            index_2+=1
            index_1+=1
    return True
            
print(one_edit_away('pale','tales'))