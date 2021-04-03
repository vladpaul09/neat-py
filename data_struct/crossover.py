class crossover:
    """ crossover """
    def __init__(self, percentage=0.8, probability_interspecies=0, probability_multipoint=0.6):
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
