from math import exp

def nn_feedforward(individual, state_input):
    number_nodes = len(individual.nodes)
    number_connections = len(individual.connections)
    # Input number + bias node
    input_nr = individual.input_nr + 1
    output_nr = individual.output_nr
    # threshold to judge if state of a node has changed significantly since last iteration
    no_change_threshold = 1e-3

    # the following code assumes node 1 and 2 inputs, node 3 bias, node 4 output, rest arbitrary (if existent, will be hidden nodes)
    # set node input steps for first timestep

    # set all node input states to zero
    for i in range(input_nr, number_nodes):
        individual.nodes[i].input_state = 0
    # node input states of the two input nodes are consecutively set to the XOR input pattern and bias node input state set to 1
    for i in range(input_nr-1):
        individual.nodes[i].input_state = state_input[i]
    individual.nodes[input_nr-1].input_state = 1
    # set node output states for first timestep (depending on input states)
    for i in range(input_nr):
        individual.nodes[i].output_state = individual.nodes[i].input_state
    for i in range(input_nr, number_nodes):
        individual.nodes[i].output_state = 1.0 / (1 + exp(-4.9 * individual.nodes[i].input_state))
    no_change_count = 0
    index_loop = 0
    while (no_change_count < number_nodes) and index_loop < 3 * number_connections:
        index_loop = index_loop + 1
        vector_node_state = [individual.nodes[i].output_state for i in range(number_nodes)]
        for index_connections in range(number_connections):
            # read relevant contents of connection gene (ID of Node where connection starts, ID of Node where it ends, and connection weight)
            ID_connection_from_node = individual.connections[index_connections].in_node
            ID_connection_to_node = individual.connections[index_connections].out_node
            connection_weight = individual.connections[index_connections].weight
            # map node ID's (as extracted from single connection genes above) to index of corresponding node in node genes matrix
            index_connection_from_node = [individual.nodes[i].id for i in range(number_nodes)].index(ID_connection_from_node)
            index_connection_to_node = [individual.nodes[i].id for i in range(number_nodes)].index(ID_connection_to_node)
            # Check if Connection is enabled
            if individual.connections[index_connections].enabled == True:
                # take output state of connection_from node, multiply with weight, add to input state of connection_to node
                individual.nodes[index_connection_to_node].input_state += individual.nodes[index_connection_from_node].output_state * connection_weight
        # pass on node input states to outputs for next timestep
        for i in range(input_nr, number_nodes):
            individual.nodes[i].output_state = 1.0 / (1 + exp(-4.9 * individual.nodes[i].input_state))
        # Re-initialize node input states for next timestep, set all output and hidden node input states to zero
        for i in range(input_nr, number_nodes):
            individual.nodes[i].input_state = 0
        # check for alle nodes where the node output state has changed by less than no_change_threshold since last iteration through all the connection genes
        vector_node_state_new = [individual.nodes[i].output_state for i in range(number_nodes)]
        no_change_count = sum([(abs(a - b)<no_change_threshold) for a, b in zip(vector_node_state_new, vector_node_state)])

    return [individual.nodes[i].output_state for i in  range(input_nr, input_nr+output_nr)]
