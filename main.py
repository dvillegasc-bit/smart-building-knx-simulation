
"""
Run and visualize the supplementary occupancy-based model.

The plotted values are dimensionless relative load indices.
They are NOT kW, kWh, measured building data, or validated energy savings.
"""

import matplotlib.pyplot as plt

from energy_model import (
    hourly_baseline,
    hourly_automated,
    saving_fraction,
    HOURS_PER_DAY,
)


def main() -> None:
    hours = list(range(HOURS_PER_DAY))
    baseline = hourly_baseline()
    automated = hourly_automated()

    baseline_total = sum(baseline)
    automated_total = sum(automated)
    reduction = saving_fraction() * 100

    print("MELBOURNE BUILDING - EXPLORATORY MODEL")
    print("-" * 48)
    print(f"Baseline daily index:   {baseline_total:.2f}")
    print(f"Automated daily index:  {automated_total:.2f}")
    print(f"Relative index change:  {reduction:.2f}%")
    print()
    print("IMPORTANT:")
    print("These are dimensionless model indices, not energy in kWh.")
    print("The result is not a measured or validated building-energy saving.")

    plt.figure(figsize=(10, 5.5))

    plt.plot(
        hours,
        baseline,
        marker="o",
        markersize=3,
        linewidth=2,
        label="Baseline scenario",
    )

    plt.plot(
        hours,
        automated,
        marker="s",
        markersize=3,
        linewidth=2,
        label="Occupancy-adjusted scenario",
    )

    plt.title(
        "Hourly Relative Load Index — Exploratory Model",
        fontsize=13,
        pad=12,
    )
    plt.xlabel("Hour of day")
    plt.ylabel("Relative load index (dimensionless)")
    plt.xticks(range(0, HOURS_PER_DAY, 2))
    plt.xlim(0, HOURS_PER_DAY - 1)
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend()
    plt.tight_layout()

    plt.savefig("results/relative_load_index.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()

