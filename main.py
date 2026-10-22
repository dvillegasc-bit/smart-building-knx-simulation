import json
import sys
from pathlib import Path
 
import matplotlib
SHOW = "--show" in sys.argv
if not SHOW:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
 
import energy_model as m
 
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)
 
# Economic inputs quoted in the project documentation (to be replaced by quotations / real tariff)
INVEST_COP = (95e6, 115e6)
TARIFF_COP_KWH = 22e6 / 35_000          # tariff IMPLIED by the quoted 22 M COP/yr saving (~628.6)
OFF_FRACTIONS = [1.0, 0.8, 0.6, 0.4, 0.2]
hours = np.arange(24)
 
# ---------- reference case (all loads at full power 24 h without automation) ----------
base, auto = m.hourly_baseline(), m.hourly_automated()
ref_saving = m.saving_fraction()
b_y, a_y = m.annual_kwh()
td_base, td_auto = m.calibrated_annual_kwh()
 
print("=== Reference case (baseline: full power 24 h) ===")
print(f"Daily  baseline / KNX : {base.sum():8.2f} / {auto.sum():8.2f} kWh/day")
print(f"Relative saving       : {ref_saving*100:8.2f} %")
print(f"Annual bottom-up      : {b_y:10,.0f} / {a_y:10,.0f} kWh/yr")
print(f"Annual top-down anchor: {td_base:10,.0f} / {td_auto:10,.0f} kWh/yr "
      f"(EUI {m.TOP_DOWN_EUI:.0f} kWh/m2/yr x {m.AREA_M2} m2 x (1-saving))")
 
# ---------- sensitivity to the baseline definition ----------
rows = []
print("\n=== Sensitivity: baseline off-hours load fraction ===")
print("off_frac  saving[%]  saved[kWh/yr]  payback[yr] (low..high invest, implied tariff)")
for f in OFF_FRACTIONS:
    s = m.saving_fraction(f)
    saved = m.top_down_baseline_kwh() * s
    pb = [m.simple_payback_years(i, saved, TARIFF_COP_KWH) for i in INVEST_COP]
    rows.append(dict(off_hours_fraction=f, saving_pct=round(s*100, 2),
                     saved_kwh_year=round(saved), payback_years_low=round(pb[0], 1),
                     payback_years_high=round(pb[1], 1)))
    print(f"{f:8.1f}  {s*100:9.2f}  {saved:13,.0f}  {pb[0]:6.1f} .. {pb[1]:.1f}")
 
json.dump(dict(reference=dict(daily_baseline_kwh=base.sum(), daily_knx_kwh=auto.sum(),
                              saving_pct=round(ref_saving*100, 2),
                              annual_bottom_up=[b_y, a_y], annual_top_down=[td_base, td_auto],
                              implied_tariff_cop_kwh=round(TARIFF_COP_KWH, 1)),
               sensitivity=rows), open(OUT / "summary.json", "w"), indent=2)
 
# ---------- figures ----------
plt.figure(figsize=(7, 4)); plt.step(hours, base, where="post", label="Baseline (no automation)")
plt.step(hours, auto, where="post", label="KNX automation")
plt.xlabel("Hour of day"); plt.ylabel("Power (kW)"); plt.title("Figure 1 - Daily load profile (reference case)")
plt.legend(); plt.grid(alpha=.3); plt.tight_layout(); plt.savefig(OUT / "figure1_profile.png", dpi=200); (None if SHOW else plt.close())
 
plt.figure(figsize=(5, 4)); bars = plt.bar(["Baseline", "KNX"], [b_y/1e3, a_y/1e3], color=["#888", "#2a7"])
plt.bar_label(bars, fmt="%.1f"); plt.ylabel("Annual energy (MWh/yr), bottom-up")
plt.title(f"Figure 2 - Annual total (saving {ref_saving*100:.1f} %)"); plt.tight_layout()
plt.savefig(OUT / "figure2_total.png", dpi=200); (None if SHOW else plt.close())
 
zb, za = m.hourly_baseline(by_zone=True), m.hourly_automated(by_zone=True)
names = [z.name for z in m.ZONES]; sav = [zb[n].sum() - za[n].sum() for n in names]
plt.figure(figsize=(6, 4)); bars = plt.bar(names, sav, color="#2a7"); plt.bar_label(bars, fmt="%.1f")
plt.ylabel("Saving (kWh/day)"); plt.title("Figure 3 - Saving by zone (reference case)")
plt.tight_layout(); plt.savefig(OUT / "figure3_savings.png", dpi=200); (None if SHOW else plt.close())
 
fig, ax = plt.subplots(figsize=(6.5, 4)); ax.plot(OFF_FRACTIONS, [r["saving_pct"] for r in rows], "o-")
ax.set_xlabel("Baseline load fraction outside 08-22 h (1.0 = original 24 h reference)")
ax.set_ylabel("Relative saving (%)"); ax.invert_xaxis(); ax.grid(alpha=.3)
ax.set_title("Figure 4 - Sensitivity of the saving to the baseline definition")
plt.tight_layout(); plt.savefig(OUT / "figure4_sensitivity.png", dpi=200); (None if SHOW else plt.close())
if SHOW:
    plt.show()
 
