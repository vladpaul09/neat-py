class Population(object):
    def __init__(self, genomes=[]):
        super(Population, self).__init__()
        self.genomes = genomes

class Genome(object):
    def __init__(self, nodes, connections, fitness, species, input_nr, output_nr):
        super(Genome, self).__init__()
        self.nodes = nodes
        self.connections = connections
        self.fitness = fitness
        self.species = species
        self.input_nr = input_nr
        self.output_nr = output_nr

class NodeGene(object):
    # nodetypes = { 1 => "Input", 2=> "Output", 3=> "Hidden", 4=>"Bias"}
    def __init__(self, id, nodetype, input_state, output_state):
        super(NodeGene, self).__init__()
        self.id = id
        self.nodetype = nodetype
        self.input_state = input_state
        self.output_state = output_state

class ConnectionGene(object):
    def __init__(self, innovation_nr, in_node, out_node, weight, enabled):
        super(ConnectionGene, self).__init__()
        self.innovation_nr = innovation_nr
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
