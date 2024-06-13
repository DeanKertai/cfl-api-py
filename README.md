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
1. Results will be saved to the `output/` folder

## Players

Picked players must be listed in the following files:

- `./picks/defence.txt`
- `./picks/kickers.txt`
- `./picks/qb.txt`
- `./picks/rb.txt`
- `./picks/wr.txt`

Each player must be on their own line, and in this format:

```
<Player ID><tab><Team Initials><tab><Player name>
```

For example:

```
159730	BC	LOKOMBO, Boseko
164128	BC	MESSAM, Isaiah
163412	BC	SAYLES, Marcus
```

If a player is added or dropped, just update the player list txt files and run the script again
