# Pokémon Data Project — PokéAPI → Python → Power BI

## Overview

This project is an end-to-end data pipeline built around **PokéAPI**.
It covers the full data workflow:

- API data extraction
- Raw data storage
- Data cleaning & normalization
- Relational data modeling
- Business-ready analytics (Power BI)

The goal is to demonstrate **data engineering and BI practices** as well as API usage.

---

## Data Sources

- **PokéAPI**: https://pokeapi.co/
- Endpoints used:
  - `/pokemon`
  - `/pokemon-species`
  - `/evolution-chain`
  - `/type`

All data is fetched programmatically using Python.

---

## Project Structure

```text
pokemon-data-project/
│
├── data_raw/                 # Raw JSON responses from PokéAPI
│   ├── pokemon/
│   └── species/
│
├── data_clean/               # Clean, normalized CSV tables
│   ├── pokemon.csv
│   ├── pokemon_stats.csv
│   ├── pokemon_types.csv
│   ├── pokemon_abilities.csv
│   ├── pokemon_species.csv
│   ├── pokemon_evolution.csv
│   └── types.csv
│
├── src/
│   ├── api/
│   │   └── pokeapi.py        # API access helpers
│   │
│   ├── processing/
│   │   ├── pokemon.py        # Pokémon-level tables
│   │   ├── species.py        # Species metadata
│   │   ├── evolution.py      # Evolution chain flattening
│   │   └── types.py          # Type reference table
│   │
│   └── utils/
│       └── io.py             # JSON / CSV helpers
│
├── notebooks/                # Exploration (not used in production)
├── powerbi/                  # Power BI report files (.pbix)
├── run_processing.py         # Pipeline runner
├── pyproject.toml            # Python project configuration
├── .gitignore
└── README.md
```