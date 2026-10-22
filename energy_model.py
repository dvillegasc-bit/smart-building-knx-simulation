
"""
Simplified occupancy-based energy model for the Melbourne Building.

This is a supplementary exploratory model, not a validated building
energy simulation and not a model of physical KNX communication.

The zone values below are illustrative model weights, NOT measured
electrical loads or verified installed power ratings.
"""

from typing import Dict, List

# Illustrative relative weights used to explore occupancy effects.
# These values are not in kW and must not be interpreted as kWh.
ZONES: Dict[str, float] = {
    "lobby": 3.0,
    "coworking": 6.0,
    "cafeteria": 5.0,
    "datacenter": 8.0,
}

HOURS_PER_DAY = 24

# Hourly occupancy factors (0.0 to 1.0).
# These are explicit modelling assumptions, not measured occupancy data.
def occupancy_factor(hour: int) -> float:
    """Return the assumed occupancy factor for an hour of the day."""
    if not 0 <= hour < HOURS_PER_DAY:
        raise ValueError("hour must be between 0 and 23")

    if 8 <= hour <= 18:
        return 1.0
    if 19 <= hour <= 22:
        return 0.5
    return 0.2


def hourly_baseline() -> List[float]:
    """
    Calculate the baseline relative load index for each hour.

    The baseline assumes every zone operates at its full relative weight.
    Results are dimensionless indices, NOT energy in kWh.
    """
    total_weight = sum(ZONES.values())
    return [total_weight for _ in range(HOURS_PER_DAY)]


def hourly_automated() -> List[float]:
    """
    Calculate an occupancy-adjusted relative load index for each hour.

    The data-centre zone is assumed to remain at its full relative weight.
    All other zones are scaled by the assumed occupancy factor.

    This is a simplified scenario, not a physical KNX or HVAC simulation.
    """
    hourly_values: List[float] = []

    for hour in range(HOURS_PER_DAY):
        occupancy = occupancy_factor(hour)
        total = 0.0

        for zone, weight in ZONES.items():
            if zone == "datacenter":
                total += weight
            else:
                total += weight * occupancy

        hourly_values.append(total)

    return hourly_values


def saving_fraction() -> float:
    """
    Return the relative reduction in the model's dimensionless daily index.

    This is not an annual energy-saving percentage.
    """
    baseline_total = sum(hourly_baseline())
    automated_total = sum(hourly_automated())

    if baseline_total <= 0:
        raise ValueError("Baseline total must be positive")

    return (baseline_total - automated_total) / baseline_total


def annual_kwh(
    daily_kwh: float,
    operating_days: int = 365,
) -> float:
    """
    Annualize a DAILY energy value, provided independently in kWh/day.

    This helper does not convert the dimensionless model index into energy.
    The input must come from a separately justified energy calculation.
    """
    if daily_kwh < 0:
        raise ValueError("daily_kwh cannot be negative")
    if operating_days < 0:
        raise ValueError("operating_days cannot be negative")

    return daily_kwh * operating_days
