"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from class_customer import Customer

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, name):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name

    def __repr__(self):
        return ''
    
    def is_open(self):
        return self.get_time() != '22:00'

    def get_time(self):
        """current time in HH:MM format,
        """
        hour = 7 + self.minutes // 60
        minutes = self.minutes % 60
        timestamp = f"{hour:02d}:{minutes:02d}" 
        return timestamp

    def print_customers(self):
        """print all customers with the current time, id, location in CSV format.
        """
        for customer in self.customers:
            print(f"{self.get_time()}, {customer.id}, {customer.location}")
        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes = self.minutes + 1
        for customer in self.customers:
            customer.next_location()
        return None
    
    def add_new_customers(self):
        """randomly creates new customers.
        """
        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more"""
        for customer in self.customers:
            customer.is_active() #Call is_active method for each customer in the list, which should return True or False
            if customer.active:
                pass
            else:
                self.customers.remove(customer)


