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
    def __init__(self, id, location) -> None:
        self.id = id
        self.location = location

    def __repr__(self) -> str:
        return f'{self.id},{self.location}'
        
    def next_location(self):

        return None

    def is_active(self):
 
        return None  