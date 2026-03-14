def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2

print(is_anagram("listen", "silent")) 
print(is_anagram("hello", "world"))  
print(is_anagram("triangle", "integral")) 