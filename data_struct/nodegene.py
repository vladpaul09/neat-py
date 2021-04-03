class NodeGene(object):

    # nodetypes = { 1 => "Input", 2=> "Output", 3=> "Hidden", 4=>"Bias"}

    def __init__(self, id, nodetype, input_state, output_state):
        super(NodeGene, self).__init__()
        self.id = id
        self.nodetype = nodetype
        self.input_state = input_state
        self.output_state = output_state
