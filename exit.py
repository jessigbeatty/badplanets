from location import *

class Exit:
 
    def __init__(self, name, leads_to):
        self.name = name
        self.leads_to = leads_to

    
to_alpha = Exit("Land on Alpha", alpha)
to_alpha_orbit = Exit("Orbit Alpha", alpha_orbit)
to_beta = Exit("Land on Beta", beta)
to_beta_orbit = Exit("Orbit Beta", beta_orbit)



