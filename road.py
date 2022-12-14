from scipy.partial import distance


# define a road class
class Road:
    def __init__(self):
        self.angle_cos = None
        self.angle_sin = None
        self.length = None

    def __init(self, start, end):
        self.start = start
        self.end = end

        self.init_properties()

    def init_properties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angle_sin = (self.end[1] - self.start[1]) / self.length
        self.angle_cos = (self.end[0] - self.start[0]) / self.length
        # These properties are used to draw the road on the screen

    def update(self, dt):
        n = len(self.vehicles)

        if n > 0:
            # Update first vehicle
            self.vehicles[0].update(None, dt)
            # Update other vehicles
            for i in range(1, n):
                lead = self.vehicles[i - 1]
                self.vehicles[i].update(lead, dt)