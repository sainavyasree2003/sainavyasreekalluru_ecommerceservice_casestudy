
import dao.OrderProcessorRepositoryImpl as imp
def main():
    while True:
            print("Ecommerce Application Menu:")
            print("1. Register Customer")
            print("2. view customer")
            print("3. update customer")
            print("4.delete customer")
            print("5.create product")
            print("6.view product")
            print("7.update product")
            print("8.delete product")
            print("9.add to cart")
            print("10.view cart")
            print("11.update cart")
            print("12.delete cart")
            print("13.place order")
            print("14.view customer order")
            print("15.update order")
            print("16.delete order")
            print("17.create order_item")
            print("18.view order_item")
            print("19.update order_item")
            print("20.delete order_item")

            choice = int(input("Enter your choice (1-20): "))
            if choice == 1:
                obj_a=imp.customers()
                obj_a.add_customer()
            elif choice == 2:
                obj_a=imp.customers()
                obj_a.select_customer()
            elif choice == 3:
                obj_a=imp.customers()
                obj_a.update_customer()
            elif choice == 4:
                obj_a=imp.customers()
                obj_a.delete_customer()
            elif choice == 5:
                obj_b=imp.products()
                obj_b.add_product()
            elif choice == 6:
                obj_b=imp.products()
                obj_b.select_product()
            elif choice == 7:
                obj_b=imp.products()
                obj_b.update_product()
            elif choice == 8:
                obj_b =imp.products()
                obj_b.delete_product()
            elif choice == 9:
                 obj_c=imp.cart()
                 obj_c.add_cart()
            elif choice == 10:
                obj_c = imp.cart()
                obj_c.select_cart()
            elif choice == 11:
                obj_c = imp.cart()
                obj_c.update_cart()
            elif choice == 12:
                obj_c = imp.cart()
                obj_c.delete_cart()
            elif choice == 13:
                obj_d=imp.orders()
                obj_d.add_order()
            elif choice == 14:
                 obj_d=imp.orders()
                 obj_d.select_order()
            elif choice == 15:
                obj_d=imp.orders()
                obj_d.update_order()
            elif choice == 16:
                obj_d=imp.orders()
                obj_d.delete_order()
            elif choice == 17:
                obj_e=imp.order_items()
                obj_e.add_orderitem()
            elif choice == 18:
                obj_e=imp.order_items()
                obj_e.select_orderitem()
            elif choice == 19:
                obj_e=imp.order_items()
                obj_e.update_orderitem()
            elif choice == 20:
                obj_e=imp.order_items()
                obj_e.delete_orderitem()
            else:
                print("Invalid choice. Please try again.")
            continue_choice=input("To continue press 'y', to stop press 'n':")
            if continue_choice.lower() == 'n':
                break

if __name__ == "__main__":
    main()



