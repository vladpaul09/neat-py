class Stagnation:

    def __init__(self, threshold=1e-2, number_generation=15):

        # threshold to judge if a species is in stagnation (max fitness of species varies below threshold)
        # this threshold is of course dependent on your fitness function, if you have a fitness function which
        # has a large spread, you might want to increase this threshold
        self.threshold = threshold

        # - If max fitness of species has stayed within stagnation.threshold in the last
        #   stagnation.number_generation generations, all its fitnesses will be reduced to 0, so it will die out
        # - Computation is done the following way: the absolute difference between the average max
        #   fitness of the last stagnation.number_generation generations and the max fitness of each
        #   of these generations is computed and compared to stagnation.threshold.
        # - If it stays within this threshold for the indicated number of generations, the species is eliminated
        self.number_generation = number_generation
