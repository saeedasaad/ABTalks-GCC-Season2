def number_of_steps(num):
    steps = 0  
    
    while num > 0:  
        if num % 2 == 0:  
            num = num // 2
        else:  
            num = num - 1
        steps += 1  
    
    return steps

user_input = int(input("Enter a positive integer: "))
result = number_of_steps(user_input)
print(f"Total steps to reduce {user_input} to zero: {result}")
