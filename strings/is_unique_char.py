"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
SOLUTION
You should first ask your interviewer if the string is an ASCII string or a Unicode string. Asking this question
will show an eye for detail and a solid foundation in computer science. We'll assume for simplicity the char­
acter set is ASCII. If this assumption is not valid, we would need to increase the storage size.
One solution is to create an array of boolean values, where the flag at index i indicates whether character
i in the alphabet is contained in the string. The second time you see this character you can immediately
return false.
We can also immediately return false if the string length exceeds the number of unique characters in the
alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.
I
It's also okay to assume 256 characters. This would be the case in extended ASCII. You should
clarify your assumptions with your interviewer.
"""

def is_unique_chars(string):
    if len(string) > 128:
        return false

    char_set = {}
    for i in range(len(string)):
        val = string[i]
        if (val in char_set):
            return False
        char_set[val] = True
    
    return True

print(is_unique_chars('abacd'))
