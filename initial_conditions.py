import constants as c



class initial_conditions():

    def __init__(self):
        self.rho = c.rho_initial


    def change_rho_0(self, percentage):
        self.rho += percentage * self.rho


    def get_P_0(self):
        return c.K * self.rho ** c.gamma


    def get_rho_0(self):
        return self.rho