from supermarket_start import Supermarket

Test_supermarket = Supermarket('Test_Supermarket')

while Test_supermarket.is_open():
    Test_supermarket.add_new_customers()
    Test_supermarket.next_minute()
    Test_supermarket.print_customers(to_csv=True)
    Test_supermarket.remove_exitsting_customers()