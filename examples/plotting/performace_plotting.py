from pathlib import Path

from dacbench.logger import load_logs, log2dataframe
from dacbench.plotting import plot_performance_per_instance, plot_performance

import matplotlib.pyplot as plt


def per_instance_example():
    file = Path("data/chainererrl_cma/PerformanceTrackingWrapper.jsonl")
    logs = load_logs(file)
    data = log2dataframe(logs, wide=True, drop_columns=["time"])
    grid = plot_performance_per_instance(data)

    grid.savefig("performance_per_instance.pdf")
    plt.show()


def performance_example():
    file = Path("data/sigmoid_example/PerformanceTrackingWrapper.jsonl")
    logs = load_logs(file)
    data = log2dataframe(logs, wide=True, drop_columns=["time"])

    # overall
    grid = plot_performance(data)
    grid.savefig("overall_performance.pdf")
    plt.show()

    # per instance seed (hue)
    grid = plot_performance(data, hue="seed")
    grid.savefig("overall_performance_per_seed_hue.pdf")
    plt.show()

    # per instance seed (hue)
    grid = plot_performance(data, col="seed", col_wrap=3)
    grid.savefig("overall_performance_per_seed.pdf")
    plt.show()


if __name__ == "__main__":
    per_instance_example()
    performance_example()
