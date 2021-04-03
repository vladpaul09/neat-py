from neat import Neat
from xor_experiment import xor_experiment

def main():
    solver = Neat(
        number_input_nodes=2,
        number_output_nodes=1,
        vector_connected_input_nodes=[1,2]
    )

    pop = xor_experiment(solver.population)

    for i in range(len(pop.genomes)):
        print(pop.genomes[i].fitness)

if __name__ == '__main__':
    main()
