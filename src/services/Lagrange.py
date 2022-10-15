from dataclasses import dataclass
from typing import Any
import numpy as np
import matplotlib.pyplot as plt
import re
import sympy as sym

@dataclass
class Lagrange:
    # x y data table
    xi: object
    
    # n number of iterations
    n: int
    
    # define x symbol
    x: str
    
    # Li(x)
    li: Any = 0

    # interpolating polynomial p(x) or fn(x)
    fnx: Any = 0

    fnx_simplified: Any = 0

    fnx_beauty: Any = 0

    def __init__(self, data: dict):
        self.data = data
        self.n = len(data["xi"])
        self.x = sym.Symbol('x')

    def get_data(self):
        return self.data
        
    def set_data(self, data: dict):
        self.data = data

    def get_n(self):
        return self.n
        
    def set_n(self, n: int):
        if n != len(self.get_data()[0]):
            self.n = len(self.get_data()[0])
        else:
            self.n = n

    def get_li(self):
        return self.li

    def set_li(self, li: Any):
        self.li = li

    def get_fnx(self):
        return self.fnx

    def set_fnx(self, fnx: Any):
        self.fnx = fnx

    def get_fnx_simplified(self):
        return self.fnx_simplified

    def set_fnx_simplified(self, fnx_simplified):
        self.fnx_simplified = fnx_simplified

    def get_fnx_beauty(self):
        return self.fnx_beauty

    def set_fnx_beauty(self, fnx_beauty: Any):
        self.fnx_beauty = fnx_beauty
    
    
    def show_data_table(self):
        print(f'|   X   | { self.get_data()["xi"] }')
        print(f'|   Y   | { self.get_data()["fi"] }')

    # method for calculate fn(x)
    def get_polinomyals(self):
        divider = np.zeros(self.get_n(), dtype= float)
        polynomial = ""
        # loop for get fn(x) term
        for i in range(0, self.get_n(), 1): 
            numerator, denominator = 1, 1
            
            # loop for get Li(x) term
            for j in range(0, self.get_n(), 1):
                if j != i:
                    numerator = numerator * ( self.x - self.get_data()["xi"][j])
                    denominator = denominator * ( self.get_data()["xi"][i] - self.get_data()["xi"][j])

            # create Li(x) = [(x - xj) * ... * (x - xn) / (xi - xj) * ... * (xn - xn)] polynomial            
            self.set_li(numerator/ denominator)

            # sum Li(x)f(xi)
            fraction = self.get_data()["fi"][i] / denominator
            self.set_fnx(self.get_fnx() + (fraction * numerator))
    
            polynomial = f'{polynomial} + [ ({self.get_data()["fi"][i]}/{denominator})*{numerator} ]'

            divider[i] = denominator

        self.set_fnx_simplified(self.get_fnx().expand())
        self.set_fnx_beauty(polynomial)


    def graph_interpolation(self):
        fnx = sym.lambdify(self.x, self.get_fnx_simplified())
        samples_number = 101
        a = np.min(self.get_data()["xi"])
        b = np.max(self.get_data()["xi"])
        fnxi = np.linspace(a, b, samples_number)
        pfi = fnx(fnxi)

        plt.plot(
            self.get_data()["xi"], 
            self.get_data()["fi"],
            'o', 
            label = 'Points'
        )
        plt.plot(fnxi,pfi, label = 'Polynomial')
        plt.legend()

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Lagrange Interpolation')
        plt.axvline(x=0, c="black", label="x=0")
        plt.axhline(y=0, c="black", label="y=0")
        plt.show()  




    