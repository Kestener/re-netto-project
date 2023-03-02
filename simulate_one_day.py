from supermarket_start import Supermarket

re_netto = Supermarket(brand = 're-netto', open='07:00', closed = '22:00')

if __name__ == "__main__":
    
    while re_netto.is_open():
        re_netto.add_new_customers()
        re_netto.next_minute()
        re_netto.print_customers()
        re_netto.remove_exitsting_customers()
