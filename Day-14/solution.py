# Problem 1
def move_zeroes(nums):
    result = [x for x in nums if x != 0]   
    zeroes = [0] * nums.count(0)          
    return result + zeroes


print(move_zeroes([0, 1, 0, 3, 12]))  

# Problem 2
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  

# Problem 3
def length_of_last_word(s):
    words = s.strip().split()   
    return len(words[-1]) if words else 0

print(length_of_last_word("Hello World"))       
print(length_of_last_word("Python Challenge ")) 