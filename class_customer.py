import numpy as np

# class Customer:
#     def __init__(self, customer_no):
#         self.customer_no = customer_no
#         self.location = "entrance"

#     def __repr__(self):
#         return f'This is customer number {self.customer_no} at {self.location}'

#     def supermarket_location(self, location):
#         self.location = location

#     def move(self):
#         location = ['checkout', 'dairy', 'drinks', 'fruit', 'spices']
#         return np.random.choice([0,1,2,3,4],p=[
#             #[c, da, dr,fr, sp]
#             [1, 0, 0, 0, 0],
#             [0.115, 0.642, 0.062, 0.103, 0.078],
#             [0.156, 0.119, 0.497, 0.121, 0.107],
#             [0.175, 0.143, 0.092, 0.521, 0.070],
#             [0.155, 0.220, 0.165, 0.139, 0.321],
#             ])
    
    # **********************************
class Customer:
    def __init__(self, customer_no):
        self.customer_no = customer_no
        self.location = "entrance"
        self.active = True
        self.probs = {"checkout" : [1, 0, 0, 0, 0, 0],
                    "dairy" : [0.095, 0.599, 0.052, 0.104, 0.085,0.065],
                    "drinks" : [0.139, 0.101, 0.455, 0.115, 0.095, 0.094],
                    "entrance" : [0.169, 0.253, 0.153, 0.033, 0.265, 0.127],
                    "fruit" : [0.137, 0.115, 0.078, 0.149, 0.466, 0.056],
                    "spices" : [0.125, 0.190, 0.147, 0.138, 0.108, 0.292]
                    }
        
    def __repr__(self):
        return f'This is customer number {self.customer_no} at {self.location}'

    def is_active(self):
        if self.location == 'checkout':
            self.active = False
        return None
    
    def move(self):
        if self.active:
            self.location = np.random.choice(["checkout","dairy","drinks","entrance","fruit","spices"],p=self.probs[self.location])
            return None
        else:
            print('Error: A checked out customer tries to move')
            return None
            
