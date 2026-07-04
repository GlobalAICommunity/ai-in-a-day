# Orbital Operations Manual — Power Systems

*Document PW-200 · Revision 3 · Classification: Crew Essential*

## 1. Overview

Orbital runs on solar power with battery storage. Solar arrays charge the batteries
during the Martian day; batteries carry the colony through night and dust events.
Managing power is mostly about **protecting the batteries** and **shedding load** when
generation drops.

## 2. Nominal power figures

| Parameter | Nominal band | Notes |
|---|---|---|
| Generation | 30 – 90 kW | Varies with sun angle and dust |
| Battery charge | 40 – 100 % | Do not let it fall below 20 % |

## 3. Dust storms

Dust is the main threat to power. Airborne dust reduces solar output and coats the
panels. A rising **dust index** usually precedes a drop in **power_kw**.

### 3.1 Dust storm response (DUST-1)
1. Expect solar generation to fall as the dust index rises above 150.
2. **Shed non-critical loads** (labs, non-essential lighting, 3D printers).
3. Prioritise life support, comms, and medical.
4. Monitor **battery_pct**; if it trends toward 20 %, shed further.
5. After the storm, **clean or allow arrays to clear** and confirm generation recovers.

## 4. Battery care

- Keep charge between 40 % and 100 % where possible.
- A single pack charging slower than its neighbour suggests **aging cells** — log for
  maintenance, do not ignore.
- Never fully discharge a pack; deep discharge permanently reduces capacity.

## 5. Load shedding priority (highest priority kept last)

1. Non-essential research equipment *(shed first)*
2. Comfort lighting and heating in unoccupied modules
3. Water reclamation *(can pause briefly)*
4. Comms
5. Medical
6. **Life support** *(never shed)*
