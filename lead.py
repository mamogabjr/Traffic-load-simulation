# Calculating IDM acceleration

alpha =0    # interaction term when lead = None
if lead:
    delta_x = lead.x - self.x - lead.1
    delta_v = self.v - lead.v
    alpha = (self.s0 + max(0, self.T*self.v +delta_v*self.v/self.sqrt_ab)) / delta_x

self.a = self.a_max * (1-(self.v/self.v_max)**4 - alpha**2)