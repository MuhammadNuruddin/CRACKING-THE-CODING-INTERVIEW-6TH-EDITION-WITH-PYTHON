"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to isSubString (e.g., "waterbottle" is a rotation of" erbottlewat").

SOLUTION
If we imagine that S2 is a rotation of S1, then we can ask what the rotation point is. For example, if you
rotate waterbottle after wat. you get erbottlewat. In a rotation, we cut S1 into two parts, x and y,
and rearrange them to get S2.
S1 = xy = waterbottle
x = wat
y = erbottle
s2 = yx = erbottlewat
So, we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2. Regardless of
where the division between x and y is, we can see that yx will always be a substring of xyxy.That is, s2 will
always be a substring of s1s1.
And this is precisely how we solve the problem: simply do isSubstring(s1s1, s2).
"""

def is_substring_rotation(string_a, string_b):
    n = len(string_a) # s1 len
    m = len(string_b) # s2 len
    # Check that s1 and s2 are equal length and not empty
    if n == m and n > 0:
        # Concatenate s1 and s1 within new buffer
        s1_s1 = string_a + string_a
        return is_substring(s1_s1, string_b)
    return False


def is_substring(string_a, string_b):
    if string_b in string_a:
        return True
    return False

# def is_substring_two(string_a, string_b):
#     string = string_a
#     substring = string_b

#     s = string.split()
#     print(s)
#     if substring in s:
#         return True
#     return False

print(is_substring_rotation('waterbottle','bottlewater'))