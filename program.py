import initial_conditions
import integrator as int
import constants as c
import plotting


def run():
    cond = initial_conditions.initial_conditions()

    tolerance = 0.01
    diff = tolerance + 1

    i = 0
    while abs(diff) > tolerance:
        integrator = int.integrator(cond)

        mass = integrator.integrate()

        diff = c.goal_mass - mass
        if diff > 0:
            diff /= c.goal_mass
        else:
            diff /= mass
        cond.change_rho_0(diff)

        print('{}: rho={}, mass = {} M_sol'.format(i, cond.rho, mass/c.solar_mass))

        i+=1

    plotting.plot_all_variables(integrator)