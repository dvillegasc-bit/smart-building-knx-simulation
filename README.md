#  Smart Building Energy Optimization using KNX Automation

This project presents a smart building energy optimization model based on a real office building in Colombia. The system integrates KNX automation, occupancy-based control strategies, and simulation to reduce energy consumption.

The results show an approximate **25% reduction in energy usage**, along with an estimated **Return on Investment (ROI) of ~4.5 years**, demonstrating both technical and economic feasibility.

---

##  Project Overview

- Simulation of energy consumption in multi-zone buildings
- KNX-based automation logic
- Occupancy-driven control strategy
- Real-world case study integration
- Energy and economic analysis

---

##  Real Building Case Study

The model is based on architectural blueprints of a real office building (~1,015.9 m²) with multiple zones:

- Auditorium (high occupancy variability)
- Coworking spaces
- Cafeteria
- Data center (constant load)
- BMS control center

This allows a realistic evaluation of energy consumption and optimization strategies.

---

##  Methodology

The total energy consumption is modeled as:

E_total = Σ (P_lighting × Occupancy + P_HVAC × Temperature) + P_static

Where:
- Occupancy varies throughout the day
- HVAC depends on thermal conditions
- Static loads include servers and critical infrastructure

---

##  Results

- Energy consumption reduced from **142,000 kWh to 107,000 kWh**
- ~25% energy savings achieved
- Highest savings observed in:
  - Auditorium
  - Coworking areas
- Data center maintained constant load for operational stability

---

##  Economic Impact

- Investment: **COP $95M – $115M (≈ USD $24k – $29k)**
- Annual savings: **COP $22,000,000 (≈ USD $5.5k)**
- ROI: **~4.5 years**

This demonstrates strong feasibility for real-world implementation.

---

##  Project Visualizations

### Energy Consumption Profile
![Energy Profile](results/figure1_profile.png)

### Total Consumption Comparison
![Total Comparison](results/figure2_total.png)

### Energy Savings
![Savings](results/figure3_savings.png)

---

##  Future Work

- Integration with real KNX hardware
- PID-based control systems
- AI-based occupancy prediction
- IoT sensor integration

---

##  Publication

This project is being prepared for submission to an IEEE conference, combining real-world implementation and simulation-based analysis.

---

##  Technologies Used

- Python
- NumPy
- Matplotlib
- KNX concepts (building automation)

---

##  Author

**Daniel Felipe Villegas Castellanos**  
Electronic Engineer  

---

##  Repository Structure


## Author

Daniel Felipe Villegas Castellanos  
Electronic Engineer | Automation & Control Systems  

📍 Colombia  
📧 dvillegasc@ucentral.edu.co  
🔗 GitHub: https://github.com/dvillegasc-bit
