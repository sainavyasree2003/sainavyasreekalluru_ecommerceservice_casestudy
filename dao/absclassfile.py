from abc import ABC,abstractmethod
class OrderProcessorRepository(ABC):
    @abstractmethod
    def create_product(self,product_id,product_name,price,product_description,stockQuantity ):
        pass

    @abstractmethod
    def create_customer(self,customer_id,customer_name,email ,customer_password ):
        pass

    @abstractmethod
    def delete_product(self,product_id):
        pass

    @abstractmethod
    def delete_customer(self,customer_id):
        pass

    @abstractmethod
    def add_cart(self,cart_id,customer_id,product_id,quantity ):
        pass

    @abstractmethod
    def delete_cart(self,cart_id ):
        pass

    @abstractmethod
    def select_cart(cart,cart_id):
        pass

    @abstractmethod
    def add_order(orders,order_id ,customer_id,order_date ,total_price ,shipping_address):
         pass

    @abstractmethod
    def select_order(cart,customer_id):
        pass


