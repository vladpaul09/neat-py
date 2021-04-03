from initial_population import initial_population
from data_struct.speciation import speciation
from pprint import pprint

class Neat(object):
    def __init__(
        self,
        number_input_nodes,
        number_output_nodes,
        average_number_non_disabled_connections=[],
        average_number_hidden_nodes=[],
        max_overall_fitness=[],
        vector_connected_input_nodes=[],
        population_size=150,
        max_generations=200,
        load_flag=0,
        save_flag=1
    ):
        super(Neat, self).__init__()
        self.number_input_nodes = number_input_nodes
        self.number_output_nodes = number_output_nodes
        self.average_number_non_disabled_connections = average_number_non_disabled_connections
        self.average_number_hidden_nodes = average_number_hidden_nodes
        self.max_overall_fitness = max_overall_fitness
        # vector of initially connected input nodes out of complete number of input nodes
        # (if you want to start with a subset and let evolution decide which ones are necessary)
        # for a fully connected initial population, uncomment the following:
        #self.vector_connected_input_nodes=[i+1 for i in range(number_input_nodes)]
        self.vector_connected_input_nodes = vector_connected_input_nodes

        self.population_size = population_size
        self.max_generations = max_generations
        self.load_flag = load_flag
        self.save_flag = save_flag

        self.speciation = speciation()

        self.population, self.innovation_record_list, self.species_record = initial_population(population_size, number_input_nodes, number_output_nodes, vector_connected_input_nodes, self.speciation)
        self.generation = 1
        
