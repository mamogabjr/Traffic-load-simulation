# setting up our speed to zero in case of a negative speed for stability
if self.v + self.a*dt < 0:
  self.x -= 1/2*self.v*self.v/self.a
  self.v = 0
else:
  self.v += self.a*dt
  self.x += self.v*dt + self.a*dt*dt/2