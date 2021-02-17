import program
import argparse
import constants as c


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--max_iterations", default=10000, type=int,
                        help="maximum number of iterations to reach solar mass. If more iterations are needed, the integration is stopped and rho is updated.")
    parser.add_argument("-m", "--goal_mass", default=1.5, type=float, help="Goal mass in solar masses")
    parser.add_argument("-r", "--rho_0", default=1., type=float, help="Density at r=0 in nuclear densities")
    parser.add_argument("-K", default=1.98183e-15, type=float, help="Adiabatic coefficient in km/m^2")
    parser.add_argument("-y", "--gamma", default=2.75, type=float, help="polytropic index")
    parser.add_argument("-t", "--tolerance", default=0.0001, type=float, help="Allowed deviation from goal mass")

    args = parser.parse_args()

    args.goal_mass *= c.SOLAR_MASS
    args.rho_0 *= c.NUCLEAR_DENSITY

    program.run(args)

    return 0


if __name__== '__main__':
    main()