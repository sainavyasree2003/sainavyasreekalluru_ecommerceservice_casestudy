import unittest

import mysql.connector as sql

import dao.OrderProcessorRepositoryImpl as imp


from myexceptions.exception import CustomerNotFoundException,OrderNotFoundException,ProductNotFoundException

class MyTestCase(unittest.TestCase):
    def test_add_product(self):
        print("enter product details to add")
        obj_b = imp.products()
        result=obj_b.add_product()
        self.assertEqual(True, result)  # add assertion here

    def test_add_cart(self):
        print("enter cart details to add")
        obj_c = imp.cart()
        result=obj_c.add_cart()
        self.assertEqual(True, result)  # add assertion here

    def test_select_orderitem(self):
        obj_d = imp.order_items()
        result = obj_d.select_orderitem()
        self.assertEqual(True, result)  # add assertion here

    def test_customer_id_not_found(self):
        # print("enter product_id details to find")
        obj_e = imp.customers()
        result=obj_e.select_customer()
        self.assertEqual(False,result)




if __name__ == '__main__':
    unittest.main()
