import numpy as np
import matplotlib.pyplot as plt
import constants as c


def plot_all_variables(integrator):
    plot_density(integrator)
    plot_pressure(integrator)
    plot_mass(integrator)


def plot_mass(integrator):
    plot_over_r(integrator, np.divide(integrator.get_masses(), c.SOLAR_MASS), 'Mass (M_sol)', xlog=True)


def plot_pressure(integrator):
    plot_over_r(integrator, integrator.get_pressures(), 'Pressure' , xlog=True)


def plot_density(integrator):
    plot_over_r(integrator, np.divide(integrator.get_densities(), c.NUCLEAR_DENSITY), 'Density', xlog=True)


def plot_over_r(integrator, values, ylabel, xlog=False, ylog=False):
    if xlog:
        plt.xscale('log')
    if ylog:
        plt.yscale('log')

    plt.ylabel(ylabel)
    plt.xlabel('r (km)')

    plt.plot(np.divide(integrator.get_rs(), 1000), values)
    plt.tight_layout()
    plt.show()

