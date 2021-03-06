import numpy as np
import constants as c


# step size (in meters)
dr = 100


# Solver for the TOV-equation relating to the internal structure of a neutron star.
class solver():
    def __init__(self, args):
        self.rho_0 = args.rho_0
        self.P_0 = args.K * self.rho_0 ** args.gamma

        # start at center (r=0) with zero mass
        self.total_mass = 0
        self.r = 0

        # save variables calculated at each step
        self.masses = []
        self.pressures = []
        self.densities = []


    # Given initial density and parameters for the EoS, integrate() returns the mass of the star.
    # If the edge of the star (P<=0) is not reached after max_iterations, the mass up until then is returned.
    def integrate(self, args):

        # initialize the variables
        P = self.P_0
        rho = self.rho_0
        r = 0

        i=0

        # loop until pressure == 0 meaning we have reached the edge of the star
        while P > 0 and i < args.max_iterations:
            r += dr

            # save all values for plotting
            self.densities.append(rho)
            self.masses.append(self.total_mass)
            self.pressures.append(P)

            # calculate rho based on P
            rho = (P / args.K) ** (1 / args.gamma)

            # increase mass based on new pressure, density and new radius
            self.total_mass += (4/3) * np.pi * (r**3 - (r-dr)** 3) * rho

            # calculate new P based on previous mass/density
            P = self.step(P, r, rho)

            i+=1
        return self.total_mass


    # Solve the TOV-equation for P_{j} --> P_{j+1}
    def step(self, P, r, rho):

        # Schwarzschild radius
        r_s = 2 * c.G * self.total_mass/c.C2

        # calculate right-hand side of the differential equation
        RHS = - ( c.G/r**2 ) * (rho + P/c.C2) * (self.total_mass + 4 * np.pi * r**3 * (P/c.C2)) / (1 - r_s/r)
        P += dr * RHS

        return P


    def get_masses(self):
        return self.masses


    def get_pressures(self):
        return self.pressures


    def get_densities(self):
        return self.densities


    def get_rs(self):
        return [dr * i for i in range(len(self.pressures))]