"""
Script to create a supermarket simulation
"""

from supermarket_start import Supermarket
from class_plot_market import PlotMarket

re_netto = Supermarket(brand = 're-netto_2', open='07:00', closed = '22:00')

while Test_supermarket.is_open():
    Test_supermarket.add_new_customers()
    Test_supermarket.print_customers(to_csv=False)
    Test_supermarket.next_minute()
    Test_supermarket.remove_exitsting_customers()

