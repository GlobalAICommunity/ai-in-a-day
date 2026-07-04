# Module 1 · Reading the colony's data 📊

> **Story:** It's morning on Orbital. Before ARIA can be smart, *you* need to understand the
> colony's raw sensor data — and teach a model to spot when something's wrong.

**Time:** ~50 min · **Beats:** 2 (both **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 1a | Explore & clean the telemetry | Core · Live-code | 25 min |
| 1b | Train an anomaly model | Core · Live-code | 25 min |

## Learning objectives

- Load and inspect a real-ish time-series dataset with **pandas**
- Handle missing values and spot outliers
- Visualise sensor trends with **matplotlib**
- Understand what an **anomaly** is and train a model to flag off-nominal readings
- Evaluate the model against known incidents

## Before you start

Make sure the dataset exists (created during setup, or run it now):

```bash
python data/generate_telemetry.py
```

This writes `data/telemetry.csv` — 7 days of 15-minute readings for Module B, including a
few **injected incidents** (a dust storm, a heater glitch, a power dip, and the big
**O₂ drop** we'll return to in the capstone).

## The data

| Column | Meaning | Nominal band |
|---|---|---|
| `timestamp` | Reading time | — |
| `habitat_temp_c` | Cabin temperature | 18–26 °C |
| `o2_pct` | Oxygen | 19.5–23.5 % |
| `co2_ppm` | Carbon dioxide | 400–1000 ppm |
| `power_kw` | Power generation | 30–90 kW |
| `battery_pct` | Battery charge | 40–100 % |
| `dust_index` | Airborne dust | 0–150 |
| `water_l` | Water reserve | 800–2000 L |
| `label` | 1 = known off-nominal (for checking our work) | — |

## Beats

### 1a · Explore & clean → [`01a_explore_clean.ipynb`](01a_explore_clean.ipynb)
Load the CSV, deal with a few missing readings, compute basic statistics, and plot O₂,
CO₂, and power over the week. Can you *see* the incidents by eye?

### 1b · Anomaly model → [`01b_anomaly_model.ipynb`](01b_anomaly_model.ipynb)
Use scikit-learn's `IsolationForest` to flag anomalous readings **without** telling it the
answers, then check how well it found the known incidents.

## 🌱 Stretch goals
- Try a supervised model (e.g. `LogisticRegression`) using the `label` column and compare.
- Add rolling-window features (e.g. 1-hour average) and see if detection improves.

## ✅ Done when
You can point at the O₂ drop on a chart **and** your model flags most of the labeled
incidents. Solutions are in [`solution/`](solution/).
