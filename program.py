import solver as s
import constants as c
import plotting


# Increase the density if the mass was lower than the goal mass. Decrease otherwise.
def update_rho(args, diff):
    args.rho_0 += diff * args.rho_0


# Get a fractional difference between goal mass and calculated mass.
# The difference is divided by the highest of the two masses, giving a result between 0 and 1.
def get_diff(mass_goal, mass_real):

    diff = mass_goal - mass_real
    diff /= max(mass_goal, mass_real)

    return diff


# runs the TOV-equation solver based on initial density (rho), goal mass and adiabatic parameters (see args).
# When goal mass is reached within the allowed tolerance, all calculated values are plotted and the loop ends.
# If not, the density is updated and the solver ran again with the new initial values.
def run(args):
    # fractional difference between calculated mass and goal mass. Initialize high enough so that while loop will start.
    diff = args.tolerance + 1

    i = 0
    while abs(diff) > args.tolerance and i < args.max_iterations:

        # Instantiate new TOV-equation solver. Initialization sets the initial rho and P.
        solver = s.solver(args)

        # run the TOV solver. Get mass of neutron star based on arguments and initial conditions.
        mass = solver.integrate(args)

        diff = get_diff(args.goal_mass, mass)

        # update the initial conditions based on the mass difference.
        update_rho(args, diff)

        print('iteration {}: rho={}, mass = {} M_sol'.format(i, args.rho_0, mass/c.SOLAR_MASS))

        i+=1

    plotting.plot_all_variables(solver)