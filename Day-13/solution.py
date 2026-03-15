def length_of_last_word(s: str) -> int:
    s = s.strip()
    
    words = s.split()
    
    last_word = words[-1]
    
    return len(last_word)

print(length_of_last_word("Hello World"))       
print(length_of_last_word("Python is fun   ")) 
print(length_of_last_word("Coding challenges build skills"))  
      