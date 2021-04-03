class mutation:
    """ mutation """
    def __init__(
        self,
        probability_add_node=0.03,
        probability_add_connection=0.05,
        probability_recurrency=0.0,
        probability_mutate_weight=0.9,
        weight_cap=8,
        weight_range=5,
        probability_gene_reenabled=0.25
    ):
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
