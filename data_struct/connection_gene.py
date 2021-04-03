class ConnectionGene(object):

    def __init__(self, innovation_nr, in_node, out_node, weight, enabled):
        super(ConnectionGene, self).__init__()
        self.innovation_nr = innovation_nr
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
