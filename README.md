# Bitcoin BIP110 Adoption Tracker

An automated tool tracking the network-wide signaling and adoption of **BIP110**, a proposal to refocus Bitcoin on its primary purpose as money.

## Live Dashboard
View the real-time interactive adoption graph here:
**[https://d18c7db.github.io/bip110-tracker/](https://d18c7db.github.io/bip110-tracker/)**

---

## About BIP110: Protecting Bitcoin's Purpose
BIP110 proposes to temporarily limit the size of data fields at the consensus level. The goal is to:
* **Correct Distorted Incentives**: Address issues caused by the standardization of support for arbitrary data.
* **Refocus Priorities**: Ensure the development and resources of the network remain focused on improving Bitcoin as a global, decentralized monetary system.

For the full technical details and the philosophy behind the proposal, visit:
**[BIP110.org](https://bip110.org/)**

---

## Project Architecture
This tracker operates entirely on GitHub's infrastructure:

1.  **Data Collection**: A GitHub Action triggers a Python script (`bip110-tracker.py`) every hour.
2.  **Network Snapshot**: The script queries [Bitnodes.io](https://bitnodes.io/) specifically for nodes signaling support for the BIP110 proposal.
3.  **Flat-File Database**: New data points (timestamp, node count, and network percentage) are appended to `data.csv`.
4.  **Frontend**: A static page using [Chart.js](https://www.chartjs.org/) renders the historical trend, pulling data directly from the CSV.

## Tracker Specs
| Feature | Details |
| :--- | :--- |
| **Data Source** | Bitnodes.io (Global Bitcoin Node Crawler) |
| **Update Interval** | Hourly (0 * * * *) |
| **Tech Stack** | Python, GitHub Actions, Chart.js, PapaParse |

---
![Hourly Scrape](https://github.com/d18c7db/bip110-tracker/actions/workflows/cron.yml/badge.svg)
