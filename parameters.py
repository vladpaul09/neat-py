class initial(object):
    """ initial setup """
    def __init__(self, kill_percentage=0.2, number_for_kill=5, number_copy=5):
        super(initial, self).__init__()
        # The percentage of each species which will be eliminated (lowest performing individuals)
        self.kill_percentage = kill_percentage
        # - The above percentage for eliminating individuals will only be used in
        #   species which have more individuals than min_number_for_kill
        # - Please note that whatever the above settings, the code always ensures
        #   that at least 2 individuals are kept to be able to cross over, or at least
        #   the single individual in a species with only one individual
        self.number_for_kill = number_for_kill
        # Species which have equal or greater than number_copy individuals
        # will have their best individual copied unchanged into the next generation
        self.number_copy = number_copy


class stagnation(object):
    def __init__(self, threshold=1e-2, number_generation=15):
        super(stagnation, self).__init__()
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

class selection(object):
    """ selection (ranking and stochastic universal sampling) """
    def __init__(self, pressure=2):
        super(selection, self).__init__()
        # Number between 1.1 and 2.0, determines selective pressure towards most fit individual of species
        selection.pressure = pressure

class refocus:
    def __init__(self, threshold=1e-2, number_generation=20):
        super(refocus, self).__init__()
        self.threshold = threshold
        # if maximum overall fitness of population doesn't change within threhold
        # for this number of generations, only the top two species are allowed to reproduce
        self.number_generation = number_generation

class speciation(object):
    def __init__(self, c1=1.0, c2=1.0, c3=0.4, threshold=3):
        super(speciation, self).__init__()
        # Speciation parameters as published by Ken Stanley
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.threshold=threshold

class crossover(object):
    """ crossover """
    def __init__(self, percentage=0.8, probability_interspecies=0, probability_multipoint=0.6):
        super(crossover, self).__init__()
        # Percentage governs the way in which new population will be composed from old population.
        # exception: species with just one individual can only use mutation
        self.percentage = percentage
        # If crossover has been selected, this probability governs the intra/interspecies
        # parent composition being used for the
        self.probability_interspecies = probability_interspecies
        # Standard-crossover in which matching connection genes are inherited randomly
        # from both parents. In the (1-crossover.probability_multipoint) cases, weights
        # of the new connection genes are the mean of the corresponding parent genes
        self.probability_multipoint = probability_multipoint


class mutation(object):
    """ mutation """
    def __init__(self, probability_add_node=0.03, probability_add_connection=0.05, probability_recurrency=0.0, probability_mutate_weight=0.9, weight_cap=8, weight_range=5, probability_gene_reenabled=0.2):
        super(mutation, self).__init__()
        self.probability_add_node = probability_add_node
        self.probability_add_connection = probability_add_connection
        # If we are in add_connection_mutation,
        # this governs if a recurrent connection is allowed.
        # Note: this will only activate if the random connection is a recurrent one,
        # otherwise the connection is simply accepted. If no possible non-recurrent connections
        # exist for the current node genes, then for e.g. a probability of 0.1, 9 times out of 10 no
        # connection is added.
        self.probability_recurrency = probability_recurrency
        self.probability_mutate_weight = probability_mutate_weight
        # Weights will be restricted from -mutation.weight_cap to mutation.weight_cap
        self.weight_cap = weight_cap
        # Random distribution with width mutation.weight_range, centered on 0. mutation
        # range of 5 will give random distribution from -2.5 to 2.5
        self.weight_range = weight_range
        # Probability of a connection gene being reenabled in offspring if it was inherited disabled
        self.probability_gene_reenabled = probability_gene_reenabled
