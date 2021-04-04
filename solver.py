from datetime import datetime
from multiprocessing import Pool

def solver(reward_function, solver, generations, print_every=1, multithreading=False, verbose=True):
    rewards_per_iteration = [0 for _ in range(generations)]
    max_rewards_per_iteration = [0 for _ in range(generations)]
    generation = 0
    while generation < generations:
        t0 = datetime.now()
        population = solver.ask()
        if multithreading:
            ### fast way = thread pool for parallelization
            with Pool(4) as pool:
                rewards = pool.map(reward_function, [individual for individual in population.genomes])
        else:
            ### slow way = loop through each "offspring"
            rewards = [reward_function(individual) for individual in population.genomes]

        population = solver.tell(rewards)
        rewards_per_iteration[generation] = sum(rewards) / len(rewards)
        max_rewards_per_iteration[generation] = max(rewards)
        if generation % print_every == 0 and verbose:
            print("Generation:", generation+1, "| Avg Reward: %.3f" % rewards_per_iteration[generation], "| Max:", max_rewards_per_iteration[generation], "| Duration:", (datetime.now() - t0))
        generation = generation + 1
    return population, rewards_per_iteration, max_rewards_per_iteration
