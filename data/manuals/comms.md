# Orbital Operations Manual — Communications

*Document CM-400 · Revision 1 · Classification: Operational*

## 1. Overview

Orbital communicates internally between modules and externally with Mission Control on
Earth. Earth communication has a light-speed delay of several minutes each way, so the
colony is expected to **handle emergencies autonomously** and report afterward.

## 2. Internal comms

- Every module has a fixed intercom panel and crew carry portable radios.
- During an incident, the crew member who first detects it **calls it out on the
  module channel** and notifies the Commander.

## 3. External comms (Earth)

| Priority | Use | Latency expectation |
|---|---|---|
| Routine | Daily status, science data | Batched, next window |
| Priority | System faults, schedule changes | Next available window |
| Emergency | Life-threatening events | Sent immediately; do not wait for a reply |

**Because of the Earth delay, never wait for Mission Control approval during a
life-support or medical emergency.** Act per the emergency procedures and report.

## 4. Comms failure

If external comms are down:
1. Continue autonomous operations.
2. Log all events with timestamps for later transmission.
3. Attempt the backup low-gain antenna.
4. Comms is a **shed-last** system during power emergencies (see Power Systems PW-200).
