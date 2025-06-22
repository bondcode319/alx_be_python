class Calculator:
    """Calculator class demonstrating static methods and class methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers using a static method.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers using a class method.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b