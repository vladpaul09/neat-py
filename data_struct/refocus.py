class refocus:

    def __init__(self, threshold=1e-2, number_generation=20):
        self.threshold = threshold
        
        # if maximum overall fitness of population doesn't change within threhold
        # for this number of generations, only the top two species are allowed to reproduce
        self.number_generation = number_generation
