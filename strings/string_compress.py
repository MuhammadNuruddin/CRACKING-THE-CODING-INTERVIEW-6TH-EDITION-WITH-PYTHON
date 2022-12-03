"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

# from collections import Counter
# def string_compress(string):
#     string = ''.join([i for i in string if i.isalpha()]).lower()
#     output = ''
#     count_chars = Counter(string)
#     for ch in count_chars:
#         output += ch + str(count_chars[ch])
#     if len(output) > len(string):
#         return string
#     else:
#         return output
#FOR SIMILAR CASE

def string_compress(string):
    string = ''.join([i for i in string if i.isalpha()]).lower()
    output = ''
    count_char = 0

    for i in range(len(string)):
        count_char+=1
        if i + 1 >= len(string) or string[i] != string[i+1]:
            output+= string[i] + str(count_char)
            count_char = 0
        
    res = output if len(output) < len(string) else string
    return res

print(string_compress('aabcccccaaa'))