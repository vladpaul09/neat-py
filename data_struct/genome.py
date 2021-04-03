class Genome(object):

    def __init__(self, nodes, connections, fitness, species, input_nr, output_nr):
        super(Genome, self).__init__()
        self.nodes = nodes
        self.connections = connections
        self.fitness = fitness
        self.species = species
