from energy_model import base_consumption, automated_consumption
import matplotlib.pyplot as plt

base = base_consumption()
auto = automated_consumption()

# Totales
total_base = base.sum()
total_auto = auto.sum()

saving = (1 - total_auto / total_base) * 100

print(f"Consumo sin automatización: {total_base:.2f} kWh")
print(f"Consumo con KNX: {total_auto:.2f} kWh")
print(f"Ahorro energético: {saving:.2f}%")

# Gráfica
hours = list(range(24))

plt.figure()
plt.plot(hours, base, label="Baseline")
plt.plot(hours, auto, label="KNX Automation")
plt.xlabel("Hour")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Energy Consumption Comparison")
plt.legend()
plt.grid()

plt.show()