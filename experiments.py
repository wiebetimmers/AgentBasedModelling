import matplotlib.pyplot as plt
import numpy as np

from gridmodel import GridModel

def happiness_experiment(n_iterations=10):
    """
    Runs the model for various 'similar_wanted' values. At the end of the run the
    average happiness is computed. This is repeated 'n_iterations' times. It then
    plots the results.
    """

    similar_wanted_values = [i/8 for i in range(9)]
    happiness_avgs = []
    happiness_stds = []

    for similar_wanted in similar_wanted_values:
        print(f"\rCalculating happiness levels for similar_wanted = {similar_wanted:.3f}", end="")
        
        happiness_values = []
        for i in range(n_iterations):
            
            model = GridModel(
                width=20, height=20,
                init_positive=190,
                init_negative=190,
                init_neutral=0,
                similar_wanted=similar_wanted
            )
            model.run()

            happiness_values.append(model.happiness/model.n_agents)

        happiness_avgs.append(np.mean(happiness_values))
        happiness_stds.append(np.std(happiness_values))

    avgs = np.array(happiness_avgs)
    stds = np.array(happiness_stds)

    plt.xlabel("Similar wanted")
    plt.ylabel("Average happiness")

    plt.plot(similar_wanted_values, happiness_avgs)
    plt.fill_between(similar_wanted_values, avgs - stds, avgs + stds, alpha=.1)
    plt.show()

if __name__ == "__main__":
    
    happiness_experiment()