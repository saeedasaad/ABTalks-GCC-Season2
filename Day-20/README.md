### Day-20: Evaluate Reverse Polish Notation (Software Engineering - Stack Evaluation)

- **Problem Statement:**  
  Evaluate an arithmetic expression written in Reverse Polish Notation (RPN).  
  - Operands are integers.  
  - Operators include `+`, `-`, `*`, `/`.  
  - Division should truncate toward zero.  

- **Challenge Overview:**  
  - Use a stack to process operands and operators.  
  - Push operands onto the stack.  
  - When encountering an operator, pop two operands, apply the operator, and push the result back.  
  - Continue until the expression is fully evaluated.  

- **Topics Covered:**  
  - Stack-based computation  
  - Expression parsing  
  - Push and pop operations  
  - Logical problem-solving techniques  
  - Interview-style coding practice  

- **Solution File:**  
  `Day-20/solution.py`

- **Reflection:**  
  This challenge reinforced how stacks simplify expression evaluation. By following the push-pop mechanism, I could process RPN expressions without worrying about operator precedence or parentheses. It highlighted the elegance of stack-based computation in compilers and calculators. Practicing this problem improved my confidence in handling stack operations and strengthened my preparation for interview-style questions. It also reminded me how foundational data structures like stacks can unlock powerful solutions in parsing and evaluation tasks.

  ---