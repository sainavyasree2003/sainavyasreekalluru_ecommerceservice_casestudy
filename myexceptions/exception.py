class CustomerNotFoundException(Exception):
    def __init__(self, message="entered customer_id is not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

class ProductNotFoundException(Exception):
    def __init__(self, message="entered product_id is not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

class OrderNotFoundException(Exception):
    def __init__(self, message="entered order_id is not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
