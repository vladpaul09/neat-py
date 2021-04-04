from neat import Neat
from xor_experiment import xor_experiment
from solver import solver

def main():

    population, rewards_mean, rewards_max = solver(
        reward_function=xor_experiment,
        generations=1,
        verbose=True,
        multithreading=False,
        solver=Neat(
            number_input_nodes=2,
            number_output_nodes=1,
            vector_connected_input_nodes=[1,2]
        )
    )
if __name__ == '__main__':
    main()
