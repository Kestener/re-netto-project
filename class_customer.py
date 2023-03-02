import numpy as np

class Customer:
    def __init__(self, customer_no):
        self.customer_no = customer_no
        self.location = "entrance"
        self.active = True
        #### Adding variable for visualisation
        self.prior_location = 'entrance'
        #### Adding variable for visualisation
        self.geo = [np.random.choice(range(70,120)),np.random.choice(range(0,15))]
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
    
    #### Function to locate customer visualy #####
    def update_geolocation(self):
        """This function returns new coordinates, if the customer changed locations. 

        Returns:
            None: The tuple self.geo will be adapted with random numbers within a threshholded location
        """
        #### Constant dictionary representing X and Y values ranges on the later supermarket plot
        LOCATION_COORDINATES = {"checkout": [0,60,0,15],
        "dairy": [35,50,25,45],
        "drinks":[8,21,25,45],
        "entrance":[70,120,0,15],
        "fruit": [90,105,25,45],
        "spices": [62,78,25,45],
        }
        #### If location did not change, keep your location, else get assigned new locations randomly 
        # (based on the valid coordinate ranges of the location itself)
        if self.location != self.prior_location:
            self.geo[0] = np.random.choice(range(LOCATION_COORDINATES[self.location][0],LOCATION_COORDINATES[self.location][1]))
            self.geo[1] = np.random.choice(range(LOCATION_COORDINATES[self.location][2],LOCATION_COORDINATES[self.location][2]))
        return None

    def move(self):
        if self.active:
            self.prior_location = self.location
            self.location = np.random.choice(["checkout","dairy","drinks","entrance","fruit","spices"],p=self.probs[self.location])
            return None
        else:
            print('Error: A checked out customer tries to move')
            return None
            

#%% 
c = Customer(123)
for list in c.probs:
    print(list)
    #print(sum(list))
# %%
