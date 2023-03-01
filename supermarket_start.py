"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from class_customer import Customer

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

######### Initiation with possible own open times ##### 

    def __init__(self,brand = 're-netto', open='07:00', closed = '22:00'):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.potential_location = ['checkout','dairy','drinks','fruit','spices']
        self.name = brand
        self.opening_time = open
        self.closing_time = closed 

#####  Added __repr__ by GK
    def __repr__(self):
        return f'''This is a supermarket object of the brand {self.name}. 
                It is opened from {self.opening_time} to {self.closing_time}'''  

#####  Added parmameter closing time by GK
    def is_open(self):
        return self.get_time() != self.closing_time

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
        
        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes = self.minutes + 1
        for customer in self.customers:
            customer.next_location()
        return None

##### Added new customer by GK
  
    def add_new_customers(self,n = 1):
        """randomly creates new customers.
        """
        
        # if wanted, controll Number of executions
        for _ in n:
            # exclusion list to secure unique numbers
            number_taken = []
            unique = False
            for customer in self.customers:
                number_taken.append(customer.customer_no)
            # loop while number is not unique
            while not unique:
                number = np.random.choice(range(9999))
                # if number not taken, create a customer with it
                if number not in number_taken:
                    self.customers.append(Customer(number))
                    unique = True
        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        return None

# if __name__ == "__main__":
    # Lidl = Supermarket("LIDL")
    # print(Lidl.get_time())
