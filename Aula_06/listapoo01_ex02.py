class Viagem:
    def __init__(self):
        self.h = 0
        self.km = 0
        self.m = 0
    def vel(self):
        return self.km/(self.h + self.m/60)
    
x = Viagem()
x.km = 300
x.h = 1
x.m = 30
print(x.h)
print(f'{x.vel()}km/h')
