from nn_feedforward import nn_feedforward

def xor_experiment(individual):


    input_pattern = [[0, 0], [0, 1], [1, 0], [1, 1]]
    output_pattern = [0, 1, 1, 0]

    outputs = []

    individual_fitness = 0
    output = []
    for index_pattern in range(4):
        output = nn_feedforward(individual, input_pattern[index_pattern])
        outputs.append(output[0])
        # prevent oscillatory connections from achieving high fitness
        individual_fitness = individual_fitness + abs(output_pattern[index_pattern] - output[0])
    # Fitness function as defined by Kenneth Stanley
    individual_fitness = (4 - individual_fitness)**2
    if sum([abs(round(a) - b) for a, b in zip(outputs, output_pattern)]) == 0:
        individual_fitness = 16
    return individual_fitness
