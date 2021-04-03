class initial:
    """ initial setup """

    def __init__(self, kill_percentage=0.2, number_for_kill=5, number_copy=5):

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
