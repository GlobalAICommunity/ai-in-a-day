# Orbital Operations Manual — Life Support Systems

*Document LS-100 · Revision 4 · Classification: Crew Essential*

## 1. Overview

The Life Support System (LSS) maintains a breathable, comfortable atmosphere across
all Orbital modules. It manages oxygen (O₂), carbon dioxide (CO₂), temperature, and
humidity. The LSS is the single most safety-critical system on the colony. When in
doubt, **protect the crew first, equipment second.**

## 2. Nominal atmosphere

| Parameter | Nominal band | Action threshold |
|---|---|---|
| Oxygen (O₂) | 19.5 – 23.5 % | Below 19.5 % → don masks |
| Carbon dioxide (CO₂) | 400 – 1000 ppm | Above 1500 ppm → evacuate module |
| Habitat temperature | 18 – 26 °C | Outside band → check heaters/coolers |

## 3. The CO₂ scrubber

Each module has a primary and a backup CO₂ scrubber. The scrubber pulls cabin air
through a filter cartridge that captures CO₂ and returns clean air. A clogged or
failed cartridge is the **most common cause of a combined O₂ drop and CO₂ rise.**

### 3.1 Scrubber fault symptoms
- O₂ percentage falling while CO₂ ppm rises **at the same time**
- Scrubber alarm on the module panel
- Audible change in scrubber fan noise

### 3.2 Scrubber recovery procedure (SCR-1)
1. **Confirm** the reading on the module panel — rule out a bad sensor.
2. **Cycle** the primary scrubber (power off 10 s, power on).
3. If levels do not recover within 15 minutes, **switch to the backup scrubber**.
4. **Replace** the filter cartridge at the next safe opportunity.
5. Log the event and notify the Commander.

## 4. Oxygen drop response (O2-DROP)

If O₂ falls below 19.5 % in any occupied module:

1. **Alert** the crew in that module immediately.
2. **Don** emergency O₂ masks.
3. If O₂ continues to fall or CO₂ exceeds 1500 ppm, **relocate crew** to the nearest
   nominal module and seal the affected one.
4. Run the **Scrubber recovery procedure (SCR-1)**.
5. Do **not** vent or open external valves to "refresh" air — this wastes reserves and
   can make things worse. Any valve action requires **Commander confirmation.**

## 5. Human-in-the-loop rule

Automated systems and assistants (including ARIA) may **recommend** actions and raise
alerts, but **must not** actuate valves, vent atmosphere, or switch life-support modes
without explicit human confirmation.
