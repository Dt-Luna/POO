class Viagem:
    def __init__(self):
        self.km = 0
        self.h = 0
        self.m = 0
        self.h += self.m/60
    def vel(self):
        return self.km/self.h
