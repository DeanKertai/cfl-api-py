# CFL Stats Analyzer v2

This is my second attempt to parse CFL player statistics for my family's fantasy football league. After breaking their public API in 2023, the CFL only provided player statistics in PDF form, which led me to try [parsing them using AI](https://github.com/DeanKertai/cfl-pdf-extractor). That worked, but it wasn't very accurate, and burning tons of coal to power ChatGPT queries just to power a small family football pool seemed a bit wasteful.

Luckily, for 2024, it appears the CFL at least has an _internal_ API used by their website which I can easily grab stats from.

This Python script grabs player statistics from the CFL website and parses it in to a format that can be used to calculate scores for league.

## Get Started

1. Install python
1. Run the script
   ```bash
   python3 main.py
   ```
