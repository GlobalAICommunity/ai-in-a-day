# Module 1 · Reading the colony's data 📊

> **Story so far:** It's the start of your day on Orbital. Before you can build a smart
> assistant, you need to understand the colony's raw sensor data — the numbers that tell you
> whether the crew is safe. In this module you'll learn to *look* at that data, tidy it up,
> and teach a computer to automatically spot when something is going wrong.

**Time:** ~50 min · **Beats:** 2 (both **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 1a | Explore & clean the telemetry | Core · Live-code | 25 min |
| 1b | Train an anomaly model | Core · Live-code | 25 min |

---

## Why we start here (and not with a chatbot)

It's tempting to jump straight to the exciting AI — talking robots, agents, all of it. But
almost every real AI system is built on top of **data**. If you don't understand your data,
your fancy model will confidently give you wrong answers. So we start where every good AI
project starts: by getting our hands on the data and really looking at it.

The good news: this module uses skills that are useful *far* beyond AI. Loading a
spreadsheet, cleaning messy values, drawing a chart, and spotting the weird points — that's
the daily bread of data science everywhere.

---

## The concepts, explained

### What is "telemetry"?
**Telemetry** just means *measurements collected automatically by sensors over time*. Your
car's dashboard is telemetry. A fitness watch is telemetry. On Orbital, sensors sample the
habitat every 15 minutes and record things like oxygen level and power output. Each row in
our data is one moment in time; each column is one thing being measured.

### What is a "time series"?
Because our readings are stamped with a time and arrive in order, this is a **time series** —
data where *order and timing matter*. "O₂ was 21% at 2pm and 18% at 3pm" tells a story that a
random pile of numbers wouldn't. We'll plot these against time so the story becomes visible.

### What is an "anomaly"?
An **anomaly** is a reading (or stretch of readings) that is *unusual* compared to normal
behaviour — often a sign that something is wrong. A CO₂ scrubber failing, a dust storm
choking the solar panels, a heater glitching: each shows up as numbers that don't look like
the calm, healthy baseline. Teaching a computer to flag anomalies automatically means the
crew doesn't have to stare at dashboards all day.

### What is a "model"?
In machine learning, a **model** is a program that has *learned a pattern from data* instead
of being told the rules by a programmer. We won't write "if O₂ < 19.5 then alarm." Instead
we'll show a model what normal looks like and let it decide what counts as strange. That
ability to learn patterns is the thread that runs through this entire day.

---

## Before you start

Make sure the dataset exists. It's produced by a small generator script (so everyone has the
exact same data). If you haven't run it yet:

```bash
python data/generate_telemetry.py
```

This writes `data/telemetry.csv` — **7 days** of readings taken every **15 minutes** for the
colony's Module B. We've deliberately hidden a few **incidents** inside it:

- a **dust storm** that saps solar power,
- a **heater glitch** that spikes the temperature,
- a brief **power dip**, and
- the big one: an **oxygen drop** on Day 5 (a failing CO₂ scrubber) — the same emergency
  ARIA will resolve in the final capstone.

Finding these is the whole point of the module.

---

## The data, column by column

| Column | What it measures | "Normal" range | Why it matters |
|---|---|---|---|
| `timestamp` | When the reading was taken | — | Lets us see trends over time |
| `module` | Which part of the colony | — | All readings here are Module B |
| `habitat_temp_c` | Cabin temperature (°C) | 18–26 | Too hot/cold is uncomfortable or dangerous |
| `o2_pct` | Oxygen (% of air) | 19.5–23.5 | Too low and the crew can't breathe |
| `co2_ppm` | Carbon dioxide (parts per million) | 400–1000 | Rises when scrubbers fail; causes headaches, then worse |
| `power_kw` | Power being generated | 30–90 | Drops during dust storms |
| `battery_pct` | Battery charge | 40–100 | The colony's safety buffer |
| `dust_index` | Airborne dust | 0–150 | High dust blocks the solar panels |
| `water_l` | Water in reserve | 800–2000 | Slowly consumed; watch the trend |
| `label` | 1 = a known incident, 0 = normal | — | **Our answer key** — we use it to check our work |

> 💡 That `label` column is a gift we gave ourselves: because *we* injected the incidents, we
> know exactly where they are. In the real world you rarely have this, but here it lets us
> *measure* whether our detective work actually caught the problems.

---

## Beats

### 1a · Explore & clean → [`01a_explore_clean.ipynb`](01a_explore_clean.ipynb)
Load the CSV into a **pandas DataFrame** (think: a spreadsheet you can control with code),
inspect it, fix a handful of missing readings, and plot O₂, CO₂, and power across the week.
By the end you should be able to *point at the oxygen drop with your finger*.

### 1b · Anomaly model → [`01b_anomaly_model.ipynb`](01b_anomaly_model.ipynb)
Use a classic machine-learning method (`IsolationForest`) that learns what "normal" looks
like and flags the outliers — **without ever being told where the incidents are**. Then we
compare its guesses to our answer key to see how well it did.

---

## 🌱 Stretch goals (optional, for when you're ahead)
- Try a **supervised** model (`LogisticRegression`) that *does* learn from the `label`
  column, and compare it to the unsupervised approach.
- Add **rolling-window features** (e.g. the average O₂ over the last hour) and see whether
  detection improves. Sometimes *how* a value is changing matters more than the value itself.

## ✅ You're done when
You can point at the O₂ drop on a chart, **and** your model flags most of the labeled
incidents. If you get stuck at any step, the fully worked answers are in
[`solution/`](solution/) — peeking is allowed; getting unstuck and moving on is the goal.
