
max_iterations = 10000


solar_mass = 1.98855e30
nuclear_density = 2.3e17

# mass we want the neutron star to be in solar masses
goal_mass = 1.5 * solar_mass

# initial density to start the program at in solar masses m^-3
rho_initial = 1. * nuclear_density

# adiabatic coefficient in kg/m
K = 1.98183e-15

# adiabatic (polytropix) index. Non-dimensional
gamma = 2.75

# gravitational constant in solar mass * m^-1 * s^-2
# G = 1.32716e20
# G = 1
G = 6.67430e-11

# speed of light in m * s^-1
c = 299792458

c2 = c**2