""" The following structure will contain various information on single species """
""" This data will be used for fitness sharing, reproduction, and for visualisation purposes """

# Species
# - Consecutive species ID's
# - Number of individuals in species
# - Matrix will be 4 rows by (number of generations existent) columns, will contain (from top to bottom)
#   number of generation, mean raw fitness, max raw fitness, and index of individual in population which
#   has produced max raw fitness

class Species(object):
    def __init__(self, id, number_individuals, generations_record=[]):
        super(Species, self).__init__()
        self.id = id
        self.number_individuals = number_individuals
        self.generations_record = generations_record

class GenerationRecord(object):
    def __init__(self, generation, mean_raw_fitness, max_raw_fitness, index_individual_max_fitness):
        super(GenerationRecord, self).__init__()
        self.generation = generation
        self.mean_raw_fitness = mean_raw_fitness
        self.max_raw_fitness = max_raw_fitness
        self.index_individual_max_fitness = index_individual_max_fitness
