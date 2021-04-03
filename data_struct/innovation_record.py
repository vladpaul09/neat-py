class InnovationRecord(object):

    def __init__(self, innovation_nr, in_node, out_node, new_node, generation_nr):
        super(InnovationRecord, self).__init__()
        self.innovation_nr = innovation_nr
        self.in_node = in_node
        self.out_node = out_node
        self.new_node = new_node
        self.generation_nr = generation_nr
