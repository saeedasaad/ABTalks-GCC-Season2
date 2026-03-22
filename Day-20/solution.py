class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:

                stack.append(int(token))
            else:

                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":

                    stack.append(int(a / b))
        
        return stack[0]

if __name__ == "__main__":
    expr1 = ["2", "1", "+", "3", "*"]   
    expr2 = ["4", "13", "5", "/", "+"]  
    expr3 = ["10", "6", "9", "3", "/", "-", "*"]  
    
    sol = Solution()
    print(sol.evalRPN(expr1))
    print(sol.evalRPN(expr2))
    print(sol.evalRPN(expr3))