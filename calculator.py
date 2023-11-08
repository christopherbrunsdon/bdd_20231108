class Calculator:
    result = None
    previous_result = None
    operation = None

    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        self.result = x / y
        return self.result

    """
    Keep track of the arithmetic operations performed on the calculator.
    """

    def arithmetic_operations(self, operation):
        self.perform_operation()
        self.operation = operation
        self.previous_result = self.result
        self.result = 0
        return self.operation

    """
    Equal operation will perform the last operation performed on the calculator.
    """

    def equal(self):
        self.perform_operation()
        self.previous_result = 0
        return self.result

    """
    Perform the arithmetic operation on the calculator.
    Clear the operation after performing it.
    """

    def perform_operation(self):
        if self.operation == "add":
            self.add(self.result, self.previous_result)
        elif self.operation == "subtract":
            self.subtract(self.result, self.previous_result)
        elif self.operation == "multiply":
            self.multiply(self.result, self.previous_result)
        elif self.operation == "divide":
            self.divide(self.result, self.previous_result)
        return self.result

