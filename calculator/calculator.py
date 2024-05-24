# create calculator class 
class Calculator:

    # add function
    def add(self, a, b): 

        return a + b

    # subtract function
    def subtract(self, a, b):
         
        return a - b

    # multiply function
    def multiply(self, a, b):

        return a * b

    # divide function 
    def divide(self, a, b):

        # denomiator can't be 0 
        if b == 0:
            raise ZeroDivisionError("Division by zero error")
        
        return a / b
