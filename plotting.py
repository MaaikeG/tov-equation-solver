import numpy as np
import matplotlib.pyplot as plt
import constants as c


# plot all the variables gather during one run of the solver
def plot_all_variables(solver):
    plot_density(solver)
    plot_pressure(solver)
    plot_mass(solver)


def plot_mass(solver):
    plot_over_r(solver, np.divide(solver.get_masses(), c.SOLAR_MASS), 'Mass (M_sol)', xlog=True)


def plot_pressure(solver):
    plot_over_r(solver, solver.get_pressures(), 'Pressure' , xlog=True)


def plot_density(solver):
    plot_over_r(solver, np.divide(solver.get_densities(), c.NUCLEAR_DENSITY), 'Density', xlog=True)


# plot given values over the radius coordinates
def plot_over_r(solver, values, ylabel, xlog=False, ylog=False):
    if xlog:
        plt.xscale('log')
    if ylog:
        plt.yscale('log')

    plt.ylabel(ylabel)
    plt.xlabel('r (km)')

    plt.plot(np.divide(solver.get_rs(), 1000), values)
    plt.tight_layout()
    plt.show()

