# * nodegenes is array 4rows * (number_input_nodes+number_output_nodes+hidden-nodes(not existent in initial population) +1 (bias-node))columns
#   nodegenes contains consecutive node ID's (upper row), node type (lower row) 1=input 2=output 3=hidden 4=bias, node input state, and node output state (used for evaluation, all input states zero initially, except bias node, which is always 1)
# * connectiongenes is array 5 rows * number_connections columns
#   from top to bottom, those five rows contain: innovation number, connection from, connection to, weight, enable bit
#   the rest of the elements in the structure for an individual should be self-explanatory

# - Innovation_record tracks innovations in a 5rows by (number of innovations) columns matrix,
#   contains innovation number, connect_from_node as well as connect_to_node for this innovation)
# - The new node (if it is a new node mutation, then this node will appear in the 4th row when
#   it is first connected. There will always be two innovations with one node mutation, since
#   there is a connection to and from the new node.
# - In the initial population, this will be abbreviated to the Node with the highest number
#   appearing in the last column of the record, since only this is needed as starting point for
#   the rest of the algorithm), and 5th row is generation this innovation occured (generation is
#   assumed to be zero for the innovations in the initial population)

from random import uniform

from data_struct.species import Species
from data_struct.population import Population
from data_struct.genome import Genome
from data_struct.nodegene import NodeGene
from data_struct.connection_gene import ConnectionGene
from data_struct.innovation_record import InnovationRecord

def initial_population(pop_nr, input_nr, output_nr, vector_connected_input_nodes, speciation):

    number_nodes = input_nr+1+output_nr
    number_connections = (len(vector_connected_input_nodes) + 1) * output_nr
    vector_connection_from = []
    vector_connection_to = []
    for i in range(output_nr):
        vector_connection_from = vector_connection_from + vector_connected_input_nodes + [input_nr + 1]

    for index_output_node in range((input_nr+2),(number_nodes)+1):
        vector_connection_to = vector_connection_to + [index_output_node for _ in range(len(vector_connected_input_nodes)+1)]
    connection_matrix = [vector_connection_from, vector_connection_to]

    population = Population()

    nodes_list = [
        [i+1 for i in range(number_nodes)],
        [1 for _ in range(input_nr)] + [4] + [2 for _ in range(output_nr)],
        [0 for _ in range(input_nr)] + [1] + [0 for _ in range(output_nr)],
        [0 for _ in range(number_nodes)]
    ]

    for _ in range(pop_nr):

        connections_list = [
            [i+1 for i in range(number_connections)],
            connection_matrix[0],
            connection_matrix[1],
            [uniform(-1, 1) for _ in range(number_connections)],
            [True for _ in range(number_connections)],
        ]

        population.genomes.append(Genome(
            nodes=[NodeGene(
                id=nodes_list[0][i],
                nodetype=nodes_list[1][i],
                input_state=nodes_list[2][i],
                output_state=nodes_list[3][i]
            ) for i in range(number_nodes)],
            connections=[ConnectionGene(
                innovation_nr=connections_list[0][i],
                in_node=connections_list[1][i],
                out_node=connections_list[2][i],
                weight=connections_list[3][i],
                enabled=connections_list[4][i]
            ) for i in range(number_connections)],
            fitness=0,
            species=0,
            input_nr=input_nr,
            output_nr=output_nr
        ))

    innovation_record_list = [InnovationRecord(
        innovation_nr=connections_list[0][i],
        in_node=connections_list[1][i],
        out_node=connections_list[2][i],
        new_node=number_nodes if i+1 == number_connections else 0,
        generation_nr=0
    ) for i in range(number_connections)]

    # initial speciation
    # put first individual in species one and update species_record
    population.genomes[0].species = 1
    # species reference matrix (abbreviated, only weights, since there are no topology differences in initial population)
    matrix_reference_individuals_weighs=[[population.genomes[0].connections[i].weight for i in range(number_connections)]]
    species_record = []
    species_record.append(Species(id=1, number_individuals=1, generation_record=[]))

    # Loop through rest of individuals and either assign to existing species or create
    # new species and use first individual of new species as reference
    for index_individual in range(1, len(population.genomes)):
        assigned_existing_species_flag = 0
        new_species_flag = 0
        index_species = 1
        # loops through the existing species, terminates when either the individual
        # is assigned to existing species or there are no more species to test it against,
        # which means it is a new species
        while assigned_existing_species_flag == 0 and new_species_flag == 0:
            # computes compatibility distance, abbreviated, only average weight distance considered
            genome_weights = [population.genomes[index_individual].connections[i].weight for i in range(number_connections)]
            distance = speciation.c3 * sum([abs(a - b) for a, b in zip(genome_weights, matrix_reference_individuals_weighs[index_species-1])]) / number_connections

            # if within threshold, assign to the existing species
            if distance < speciation.threshold:
                population.genomes[index_individual].species = index_species
                assigned_existing_species_flag = 1
                species_record[index_species-1].number_individuals += 1
            index_species = index_species + 1
            # Outside of species references, must be new species
            if index_species > len(matrix_reference_individuals_weighs) and assigned_existing_species_flag == 0:
                new_species_flag = 1
        # check for new species, if it is, update the species_record and use individual
        # as reference for new species
        if new_species_flag == 1:
            population.genomes[index_individual].species = index_species
            matrix_reference_individuals_weighs.append([population.genomes[index_individual].connections[i].weight for i in range(number_connections)])
            # if number individuals in a species is zero, that species is extinct
            species_record.append(Species(id=index_species, number_individuals=1, generation_record=[]))


    return population, innovation_record_list, species_record
