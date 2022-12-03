"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

SOLUTION
A common approach in string manipulation problems is to edit the string starting from the end and working
backwards. This is useful because we have an extra buffer at the end, which allows us to change characters
without worrying about what we're overwriting.

We will use this approach in this problem. The algorithm employs a two-scan approach. In the first scan, we
count the number of spaces. By tripling this number, we can compute how many extra characters we will
have in the final string. In the second pass, which is done in reverse order, we actually edit the string. When
we see a space, we replace it with %20. If there is no space, then we copy the original character.
"""
def replace_spaces(string, true_length):
    space_count, index = 0, 0
    string = list(string)
    for i in range(true_length):
        if string[i] == ' ':
            space_count+= 1
    index = true_length + space_count * 2
    if true_length < len(string):
        string[true_length] = '\0'
    
    for i in range(true_length - 1,-1,-1):
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    string = ''.join([str(elem) for elem in string])
    return string


string = 'Welcome to the search       '
print(replace_spaces(string, 21))