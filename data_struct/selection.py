class selection:
    """ selection (ranking and stochastic universal sampling) """

    def __init__(self, pressure=2):
        # Number between 1.1 and 2.0, determines selective pressure towards most fit individual of species
        selection.pressure = pressure
