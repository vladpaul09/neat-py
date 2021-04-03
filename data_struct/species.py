class Species(object):
    """ The following structure will contain various information on single species """
    """ This data will be used for fitness sharing, reproduction, and for visualisation purposes """

    # Species
    # - Consecutive species ID's
    # - Number of individuals in species
    # - Matrix will be 4 rows by (number of generations existent) columns, will contain (from top to bottom)
    #   number of generation, mean raw fitness, max raw fitness, and index of individual in population which
    #   has produced max raw fitness

    def __init__(self, id, number_individuals, generation_record):
        super(Species, self).__init__()
        self.id = id
        self.number_individuals = number_individuals
        self.generation_record = generation_record
