import numpy as np
import math

class Integrator:
    def __init__(self, x_min, x_max, N):
        self.x_min = x_min
        self.x_max = x_max
        self.N = N
        self.result = 0

    def _f(self, x):
        return (x**2 * math.e**(-x) * math.sin(x))

    def integrate(self):
        for i in range(0,self.N):
            d_x = (self.x_max - self.x_min)/ self.N
            x_i = self.x_min + i * d_x
            self.result += self._f(x_i) * d_x

    def show(self):
        print(self.result)


i = Integrator(1, 3, 200000)
i.integrate()
i.show()
