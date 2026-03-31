import numpy as np

# Parámetros por zona (kWh por hora)
zones = {
    "lobby": 3,
    "coworking": 6,
    "cafeteria": 5,
    "datacenter": 8
}

def occupancy(hour):
    """Modelo simple de ocupación"""
    if 8 <= hour <= 18:
        return 1.0  # alta ocupación
    elif 18 < hour <= 22:
        return 0.5  # media
    else:
        return 0.2  # baja

def base_consumption():
    """Consumo sin automatización"""
    consumption = []
    for h in range(24):
        total = sum(zones.values())
        consumption.append(total)
    return np.array(consumption)

def automated_consumption():
    """Consumo con automatización KNX"""
    consumption = []
    for h in range(24):
        occ = occupancy(h)
        total = 0
        
        for zone, base in zones.items():
            if zone == "datacenter":
                # siempre activo
                total += base
            else:
                # control por ocupación
                total += base * occ
        
        consumption.append(total)
    
    return np.array(consumption)