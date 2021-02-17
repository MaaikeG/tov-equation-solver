import integrator as int
import constants as c
import plotting


def update_rho(args, diff):
    args.rho_0 += diff * args.rho_0


def get_diff(mass_goal, mass_real):
    diff = mass_goal - mass_real

    if diff > 0:
        diff /= mass_goal
    else:
        diff /= mass_real
    return diff


def run(args):
    # fractional difference between calculated mass and goal mass. Initialize high enough so that while loop will start.
    diff = args.tolerance + 1

    i = 0
    while abs(diff) > args.tolerance:

        # Instantiate new integrator which sets the initial rho and P
        integrator = int.integrator(args)

        # run the solver. Get mass of neutron star based on arguments and initial conditions
        mass = integrator.integrate(args)

        diff = get_diff(args.goal_mass, mass)

        # update the initial conditions based on the mass difference
        update_rho(args, diff)

        print('iteration {}: rho={}, mass = {} M_sol'.format(i, args.rho_0, mass/c.SOLAR_MASS))

        i+=1

    plotting.plot_all_variables(integrator)