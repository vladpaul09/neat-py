from nn_feedforward import nn_feedforward

def xor_experiment(population):

    number_individuals=len(population.genomes)

    input_pattern = [[0, 0], [0, 1], [1, 0], [1, 1]]
    output_pattern = [0, 1, 1, 0]

    outputs = []

    for index_individual in range(number_individuals):
        number_nodes = len(population.genomes[index_individual].nodes)
        number_connections = len(population.genomes[index_individual].connections)
        individual_fitness = 0
        output = []
        for index_pattern in range(4):
            output = nn_feedforward(population.genomes[index_individual], number_nodes, number_connections, input_pattern[index_pattern])
            outputs.append(output)
            # prevent oscillatory connections from achieving high fitness
            individual_fitness = individual_fitness + abs(output_pattern[index_pattern] - output)
        # Fitness function as defined by Kenneth Stanley
        population.genomes[index_individual].fitness = (4 - individual_fitness)**2
        if sum([abs(round(a) - b) for a, b in zip(outputs, output_pattern)]) == 0:
            population.genomes[index_individual].fitness = 16

    return population
