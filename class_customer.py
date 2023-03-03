"""
Module of Customer class for the Markov chain simulation
"""

import numpy as np

class Customer:
    """Constructs a customer with its movement probabilities"""
    def __init__(self, customer_no):
        self.customer_no = customer_no
        self.location = "entrance"
        self.active = True
        self.probs = {"checkout" : [1, 0, 0, 0, 0, 0],
                    "dairy" : [0.095, 0.598, 0.053, 0.104, 0.085,0.065],
                    "drinks" : [0.139, 0.101, 0.455, 0.115, 0.095, 0.095],
                    "entrance" : [0.169, 0.253, 0.153, 0.033, 0.265, 0.127],
                    "fruit" : [0.136, 0.115, 0.078, 0.149, 0.466, 0.056],
                    "spices" : [0.125, 0.190, 0.147, 0.138, 0.108, 0.292]
                    }

    def __repr__(self):
        return f'This is customer number {self.customer_no} at {self.location}'

    def is_active(self):
        """Checks customer location and updated the active attribute accordingly"""
        if self.location == 'checkout':
            self.active = False

    def move(self):
        """Moves the customer around the supermarket based on the probabilities matrix"""
        if self.active:
            self.location = np.random.choice(["checkout","dairy","drinks",
                                              "entrance","fruit","spices"],
                                             p=self.probs[self.location])
        else:
            print('Error: A checked out customer tries to move')
