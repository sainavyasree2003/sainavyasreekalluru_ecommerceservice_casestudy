
import mysql.connector as sql
import datetime
from myexceptions.exception import CustomerNotFoundException,OrderNotFoundException,ProductNotFoundException
class main1:
    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='ecommercewebservice', user='root', password='9392951228')
            if self.conn.is_connected:
                 print('Database is Connected:')
            else:
                  print('Not Connected with Database')
            self.stmt = self.conn.cursor()
            return True
        except Exception as e:
            print(f'Raised DataBaseConnection:{e}')
        return False

    def close(self):
        self.conn.close()
obj=main1()
obj.open()


class customers(main1):
    def _init_(self):
        self.customer_id = ''
        self.customer_name = ''
        self.email = ''
        self.customer_password = ''

        print(self.customer_id, self.customer_name, self.email, self.customer_password)

    def create_customer(self):
        try:
          create_str = '''create table if not exists customers(customer_id int primary key auto_increment,
                        customer_name varchar(50),
                        email varchar(50),
                        customer_password varchar(50))'''

          self.open()
          self.stmt.execute(create_str)
          self.stmt.close()
          print('Table created successfully-------:')
        except Exception as e:
            print(f"error creating table customers:{e}")

    def add_customer(self):
        try:
            self.customer_id = int(input('Enter customer_id:'))
            self.customer_name = input('Enter name:')
            self.email = input('Enter email:')
            self.customer_password = int(input('Enter password:'))
            print(self.customer_id, self.customer_name, self.email, self.customer_password)

            data = [(self.customer_id, self.customer_name, self.email, self.customer_password)]

            insert_str = '''insert into customers(customer_id,customer_name,email,customer_password )
                   values (%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print('--customer registered successfully--')
        except Exception as e:
            print(f"error in inserting customer:{e}")
        finally:
             self.close()

    def select_customer(self):
        try:
            self.open()
            self.customer_id=int(input("enter customer_id:"))
            select_str = '''select * from customers where customer_id = %s'''
            data =[self.customer_id]
            self.stmt.execute(select_str, data)
            records = self.stmt.fetchall()
            #print('')
            if records:
              print('_______Records In Customers Table___')
            for i in records:
                print(i)
                return True
            else:
                   raise CustomerNotFoundException("entered customer_id is not found")

        except CustomerNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e)+"---error in getting customer_id:---")
        finally:
            self.close()


    def update_customer(self):
        try:
            self.customer_id = int(input('Enter customer_id which is to be updated:'))
            self.customer_name = input('Enter name:')
            self.email = input('Enter email:')
            self.customer_password = int(input('Enter password:'))
            update_str = 'update customers set customer_name =%s,email = %s,customer_password= %s where customer_id=%s'
            self.open()

            data = [(self.customer_name, self.email, self.customer_password, self.customer_id)]

            self.stmt.executemany(update_str, data)
            self.conn.commit()
            if self.stmt.rowcount==0:
                print(f"no records found to update for customer_id:{self.customer_id}.")
            else:
                print(update_str, data)
                print('Records updated successfully...')
        except Exception as e:
            print(f"error in updating customer:{e}")

    def delete_customer(self):
        try:
           self.customer_id = input('enter the customer_id to be deleted:')
           delete_str = 'delete from customers where customer_id= %s'
           data = [self.customer_id]
           self.open()
           self.stmt.execute(delete_str, data)
           self.conn.commit()
           if self.stmt.rowcount == 0:
              print('No records found to delete.')
           else:
            print('Records Deleted Successfully--------')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            self.close()


class products(main1):
    def _init_(self):
        self.product_id = ''
        self.product_name = ''
        self.price = ''
        self.product_description = ''
        self.stockQuantity = ''
        print(self.product_id, self.product_name, self.price, self.product_description, self.stockQuantity)

    def create_product(self):
        try:
            create_str = '''create table if not exists products(product_id int primary key auto_increment,
                        product_name varchar(50),
                        price int,
                        product_description varchar(50),
                        stockQuantity int) 
                        '''
            self.open()
            self.stmt.execute(create_str)
            self.stmt.close()
            print('Table created successfully-------:')
        except Exception as e:
            print(f"error creating table customers:{e}")

    def add_product(self):
        try:
           self.product_id = int(input('Enter product_id:'))
           self.product_name = input('Enter name:')
           self.price = int(input('Enter price:'))
           self.product_description = input('Enter product_description:')
           self.stockQuantity = int(input("enter stockQuantity:"))
           print(self.product_id, self.product_name, self.price, self.product_description, self.stockQuantity)

           data = [
            (self.product_id, self.product_name, self.price, self.product_description, self.stockQuantity)]

           insert_str = '''insert into products(product_id,product_name,price,product_description,stockQuantity )
                   values (%s,%s,%s,%s,%s)'''
           self.open()
           self.stmt.executemany(insert_str, data)
           self.conn.commit()
           print('Records Inserted Successfully--')
           return True
        except Exception as e:
            print(f"error in inserting product:{e}")
        finally:
             self.close()


    def select_product(self):
        try:
            self.product_id=int(input("enter product_id:"))
            select_str = '''select * from products where product_id= %s'''
            data=[self.product_id]
            self.open()
            self.stmt.execute(select_str, data)
            records = self.stmt.fetchall()
            print('')
            if records:
              print('_______Records In products Table___')
            for i in records:
                print(i)
            else:
                self.close()
            raise ProductNotFoundException("entered product_id is not found")

        except ProductNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e)+"---error in getting product_id:---")


    def update_product(self):
        try:
            self.select_product()
            self.product_id = int(input('Enter product_id which is to be updated:'))
            self.product_name = input('Enter name:')
            self.price = int(input('Enter price:'))
            self.product_description = input('Enter product_description:')
            self.stockQuantity = int(input("enter stockQuantity"))
            update_str = 'update products set product_name =%s,price = %s,product_description= %s,stockQuantity=%s where product_id = %s'
            self.open()

            data = [(self.product_id, self.product_name, self.price, self.product_description,
                 self.stockQuantity)]

            self.stmt.executemany(update_str, data)
            self.conn.commit()
            if self.stmt.rowcount == 0:
                print(f"no records found to update for customer_id{self.customer_id}.")
            else:
                print(update_str, data)
                print('Records updated successfully...')
        except Exception as e:
            print(f"error updating table products:{e}")

    def delete_product(self):
        try:
           product_id = input('enter the product_id to be deleted:')
           delete_str = 'delete from products where product_id=%s'
           data = [product_id]
           self.open()
           self.stmt.execute(delete_str, data)
           self.conn.commit()
           if self.stmt.rowcount == 0:
              print('No records found to delete.')
           else:
               print('Records Deleted Successfully--------')
        except Exception as e:
            print(f"error deleting table products:{e}")


class cart(main1):
    def _init_(self):
        self.cart_id = ''
        self.customer_id = ''
        self.product_id = ''
        self.quantity = ''
        print(self.cart_id, self.customer_id, self.product_id, self.quantity)

    def create_cart(self):
        try:
            create_str = '''create table if not exists cart(cart_id int primary key auto_increment,
                        customer_id int references customers(customer_id) on delete cascade,
                        product_id int references products(product_id) on delete cascade,
                        quantity int
                        '''

            self.open()
            self.stmt.execute(create_str)
            self.stmt.close()
            print('Table created successfully-------:')
        except Exception as e:
            print(f"error creating table cart:{e}")

    def add_cart(self):
        try:
            self.cart_id = int(input('Enter cart_id:'))
            self.customer_id = int(input('Enter customer_id:'))
            self.product_id = int(input('Enter product_id:'))
            self.quantity = int(input("enter quantity"))
            print(self.cart_id, self.customer_id, self.product_id, self.quantity)

            data = [(self.cart_id, self.customer_id, self.product_id, self.quantity)]

            insert_str = '''insert into cart(cart_id,customer_id,product_id,quantity )
                   values (%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print('Records Inserted Successfully--')
            return True
        except Exception as e:
            print(f"error in inserting cart:{e}")
        finally:
            self.close()


    def select_cart(self):
        try:
            self.customer_id=int(input("enter  customer_id for displaying products in cart:"))
            select_str = '''select p.product_id,p.product_name,p.price,c.quantity from cart c join products p on c.product_id=p.product_id  where customer_id=%s'''
            self.open()
            data=[self.customer_id]
            self.stmt.execute(select_str, data)
            records = self.stmt.fetchall()
            print('')
            print('_______Records In cart Table___')
            for i in records:
                print(i)
                return True
            else:
                raise CustomerNotFoundException("entered customer_id is not found")
        except CustomerNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---error in getting customer_id:---")
        finally:
            self.close()


    def update_cart(self):
        try:
           self.cart_id = int(input('Enter cart_id that has to be updated:'))
           self.customer_id = int(input('enter customer_id: '))
           self.product_id = int(input('Enter product_id:'))
           self.quantity = int(input('quantity:'))

           update_str = 'update cart set customer_id =%s,product_id = %s,quantity=%s where cart_id = %s'
           self.open()

           data = [(self.cart_id, self.customer_id, self.product_id, self.quantity)]

           self.stmt.executemany(update_str, data)
           self.conn.commit()
           if self.stmt.rowcount == 0:
                print(f"no records found to update for customer_id{self.customer_id}.")
           else:
            print(update_str, data)
            print('Records updated successfully...')
        except Exception as e:
            print(f"error updating cart table:{e}")

    def delete_cart(self):
        try:
           customer_id= int(input('enter the customer_id to be deleted:'))
           product_id= int(input('enter the product_id to be deleted:'))
           delete_str = 'delete from cart where customer_id=%s and product_id=%s'
           data = [(customer_id,product_id)]
           self.open()
           self.stmt.executemany(delete_str, data)
           self.conn.commit()
           if self.stmt.rowcount == 0:
              print('No records found to delete.')
           else:
            print('Records Deleted Successfully--------')
        except Exception as e:
            print(f'An error occurred: {e}')


class orders(main1):
    def _init_(self):
        self.order_id = ''
        self.customer_id = ''
        self.order_date = ''
        self.total_price = ''
        self.shipping_address = ''
        print(self.order_id, self.customer_id, self.order_date, self.total_price, self.shipping_address)

    def create_order(self):
        try:
            create_str = '''create table if not exists orders(order_id int primary key auto_increment,
                        customer_id int references customers(customer_id) on delete cascade,
                        order_date date,
                        total_price int,
                        shipping_address varchar(50))
                        '''

            self.open()
            self.stmt.execute(create_str)
            self.stmt.close()
            print('Table created successfully-------:')
        except Exception as e:
            print(f"error creating table orders:{e}")

    def add_order(self):
        try:
            self.order_id = int(input('Enter order_id:'))
            self.customer_id = int(input('Enter customer_id:'))
            self.order_date = input('Enter order_date: ')
            self.total_price = int(input("total_price: "))
            self.shipping_address = input('enter shipping_address:')
            print(self.order_id, self.customer_id, self.order_date, self.total_price, self.shipping_address)

            data = [(self.order_id, self.customer_id, self.order_date, self.total_price, self.shipping_address)]

            insert_str = '''insert into orders(order_id,customer_id,order_date,total_price,shipping_address )
                   values (%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print('Records Inserted Successfully--')
        except Exception as e:
            print(f"error in inserting customer:{e}")
        finally:
            self.close()


    def select_order(self):
        try:
            self.customer_id=int(input("enter customer_id for which orders are to be displayed:"))
            select_str = '''select * from orders where customer_id=%s'''
            self.open()
            data=[self.customer_id]
            self.stmt.execute(select_str, data)
            records = self.stmt.fetchall()
            print('')
            if records:
                  print('_______Records In orders Table___')
                  for i in records:
                        print(i)
                  return True
            else:
                 self.close()
            raise OrderNotFoundException(" order_id is not found for entered customer_id")

        except OrderNotFoundException as e:
             print(e)
        except Exception as e:
              print(str(e) + "---error in getting order_id:---")


    def update_order(self):
        try:
            self.order_id = int(input('Enter order_id that has to be updated:'))
            self.customer_id = int(input('Enter customer_id :'))
            self.order_date = input('Enter order_date: ')
            self.total_price = int(input("total_price: "))
            self.shipping_address = input('enter shipping_address:')
            update_str = 'update orders set customer_id = %s,order_date = %s,total_price=%s,shipping_address=%s where order_id=%s'
            self.open()

            data = [( self.customer_id, self.order_date, self.total_price, self.shipping_address,self.order_id)]

            self.stmt.executemany(update_str, data)
            self.conn.commit()
            if self.stmt.rowcount == 0:
                print(f"no records found to update for customer_id{self.customer_id}.")
            else:
                print(update_str, data)
                print('Records updated successfully...')
        except Exception as e:
            print(f"error updating table orders:{e}")
    def delete_order(self):
        try:
            order_id = int(input('enter the order_id to be deleted:'))
            delete_str = 'delete from orders where order_id=%s'
            data = [order_id]
            self.open()
            self.stmt.execute(delete_str, data)
            self.conn.commit()
            if self.stmt.rowcount == 0:
                print('No records found to delete.')
            else:
                print('Records Deleted Successfully--------')
        except Exception as e:
            print(f"error while deleting:{e}")

class order_items(main1):
    def _init_(self):
        self.order_item_id = ''
        self.order_id = ''
        self.product_id = ''
        self.quantity = ''
        print(self.order_item_id, self.order_id, self.product_id, self.quantity)

    def create_orderitem(self):
        try:
            create_str = '''create table if not exists order_items(order_item_id int primary key auto_increment,
                        order_id int references orders(order_id) on delete cascade,
                        product_id int references products(product_id) on delete cascade,
                        quantity int )
                        '''

            self.open()
            self.stmt.execute(create_str)
            self.stmt.close()
            print('Table created successfully-------:')
        except Exception as e:
            print(f"error creating table order_items:{e}")

    def add_orderitem(self):
        try:
            self.order_item_id = int(input('Enter order_item_id:'))
            self.order_id = int(input('Enter order_id:'))
            self.product_id = int(input('Enter product_id: '))
            self.quantity = int(input("quantity: "))
            print(self.order_item_id, self.order_id, self.product_id, self.quantity)

            data = [(self.order_item_id, self.order_id, self.product_id, self.quantity)]

            insert_str = '''insert into order_items(order_item_id,order_id,product_id,quantity)
                   values (%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print('Records Inserted Successfully--')
        except Exception as e:
            print(f"error in inserting customer:{e}")
        finally:
            self.close()

    def select_orderitem(self):
        try:
            self.product_id=int(input("enter product_id to find whether ordered or not:"))
            data=[self.product_id]
            select_str = '''select * from order_items where product_id=%s'''
            self.open()
            self.stmt.execute(select_str, data)
            records = self.stmt.fetchall()
            print('')
            print('_______Records In cart Table___')
            for i in records:
              print(i)
            return True

        except Exception as e:
             print(f"error while getting order_items:{e}")
        finally:
            self.close()


def update_orderitem(self):
    try:
        self.order_item_id = int(input('Enter order_item_id which is to be updated:'))
        self.order_id = int(input('Enter order_id:'))
        self.product_id = int(input('Enter product_id: '))
        self.quantity = int(input("quantity: "))
        update_str = 'update order_items set order_id =%s,product_id = %s,quantity=%s where order_item_id = %s'
        self.open()

        data = [(self.order_item_id, self.order_id, self.product_id, self.quantity)]

        self.stmt.executemany(update_str, data)
        self.conn.commit()
        if self.stmt.rowcount == 0:
            print(f"no records found to update for customer_id{self.customer_id}.")
        else:
            print(update_str, data)
            print('Records updated successfully...')
    except Exception as e:
        print(f'error updating table: {e}')

    def delete_orderitem(self):
        try:
            order_item_id = int(input('enter the order_item_id to be deleted:'))
            delete_str = f'delete from order_items where order_item_id=%s'
            data = [order_item_id]
            self.open()
            self.stmt.execute(delete_str, data)
            self.conn.commit()
            if self.stmt.rowcount == 0:
               print('No records found to delete.')
            else:
               print('Records Deleted Successfully--------')
        except Exception as e:
           print(f"error creating table customers:{e}")


obj1 = customers()
#obj1.create_customer()
#obj1.add_customer()
#obj1.select_customer()
#obj1.update_customer()
#obj1.delete_customer()
obj2 = products()
#obj2.create_product()
#obj2.select_product()
#obj2.add_product()
#obj2.update_product()
#obj2.delete_product()19
obj3 = cart()
#obj3.create_cart()
#obj3.add_cart()
#obj3.select_cart()
#obj3.update_cart()
#obj3.delete_cart()
obj4 = orders()
#obj4=create_order()
#obj4.add_order()
#obj4.select_order()
#obj4.update_order()
#obj4.delete_order()
obj5 = order_items()
#obj5.create_orderitem()
#obj5.add_orderitem()
#obj5.select_orderitem()
#obj5.update_orderitem()
#obj5.delete_orderitem()








