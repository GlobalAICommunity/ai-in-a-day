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
the daily bread of data science everywhere, and it's also just genuinely useful for
understanding *any* system that produces numbers over time, AI-related or not.

One more reason this comes first: everything ARIA does later in the day is only as good as
the data underneath it. In Module 3 you'll see an AI model confidently invent a fact; in
Module 4 you'll fix that by grounding it in real documents. That same lesson — *garbage in,
garbage out* — applies here too. A model trained on messy, uninspected data will learn the
mess, not the truth. So today's very first skill, before any "AI magic," is simply: **look at
your data before you trust anything built on top of it.**

---

## The concepts, explained

### What is a CSV file, and what is a DataFrame?
A **CSV** ("comma-separated values") file is one of the simplest possible ways to store a
table as plain text: each line is one row, and commas separate the columns. You could open
`telemetry.csv` in a text editor and read it, but it would be tedious to work with by eye. In
the notebook, we'll load it with a library called **pandas** into a structure called a
**DataFrame** — think of it as a spreadsheet you control entirely with code: you can filter
rows, compute averages, and draw charts with a single line, instead of clicking around a
spreadsheet app. Almost every data task in Python starts by getting your data into a
DataFrame, so this is a foundational skill you'll reuse constantly, in this workshop and
beyond.

### What is "telemetry"?
**Telemetry** just means *measurements collected automatically by sensors over time*. Your
car's dashboard is telemetry. A fitness watch is telemetry. On Orbital, sensors sample the
habitat every 15 minutes and record things like oxygen level and power output. Each row in
our data is one moment in time; each column is one thing being measured.

### What is a "time series"?
Because our readings are stamped with a time and arrive in order, this is a **time series** —
data where *order and timing matter*. "O₂ was 21% at 2pm and 18% at 3pm" tells a story that a
random pile of numbers wouldn't. We'll plot these against time — draw a line chart with time
on the horizontal axis and the sensor value on the vertical axis — so the story becomes
visible at a glance instead of buried in a table of numbers.

### What is an "anomaly"?
An **anomaly** is a reading (or stretch of readings) that is *unusual* compared to normal
behaviour — often a sign that something is wrong. A CO₂ scrubber failing, a dust storm
choking the solar panels, a heater glitching: each shows up as numbers that don't look like
the calm, healthy baseline. Teaching a computer to flag anomalies automatically means the
crew doesn't have to stare at dashboards all day, watching for a problem that might only show
up once a week.

### What is a "model"?
In machine learning, a **model** is a program that has *learned a pattern from data* instead
of being told the rules by a programmer. We won't write "if O₂ < 19.5 then alarm." Instead
we'll show a model what normal looks like and let it decide what counts as strange — which
matters because in a real colony, "normal" for one sensor on one day might look different
from "normal" on another day, and hard-coded thresholds can't adapt to that the way a learned
pattern can. That ability to learn patterns instead of following fixed rules is the thread
that runs through this entire day — every module from here on is really just a different
flavour of "a model learned something useful and we're putting it to work."

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
Load the CSV into a **pandas DataFrame**, inspect it, fix a handful of missing readings, and
plot O₂, CO₂, and power across the week. "Cleaning" here mostly means deciding what to do
about gaps and obviously-wrong values — a sensor that briefly dropped out, say — so that later
steps aren't confused by holes in the data. By the end you should be able to *point at the
oxygen drop with your finger* on a chart.

### 1b · Anomaly model → [`01b_anomaly_model.ipynb`](01b_anomaly_model.ipynb)
Use a classic machine-learning method (`IsolationForest`) that learns what "normal" looks
like and flags the outliers — **without ever being told where the incidents are**. This is
called **unsupervised learning**: the model isn't shown an answer key while it learns, it just
looks for points that are structurally different from the rest. Then we compare its guesses to
our answer key (the `label` column) to see how well it did — our first taste of *evaluating* a
model rather than just trusting it.

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
