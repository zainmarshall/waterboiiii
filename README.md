# Waterboiiii (Package Style)

Water Quality Science Olympiad ID bot using `sciolyid` as an installed package.

## Repo layout

- `water_quality_bot.py` bot config + startup
- `water_quality_data/` item lists, groups, wiki links
- `water-quality-images/` image dataset repo + scraper
- `setup.sh.example` token env template

## Setup

```sh
cd /Users/zain/Developer/waterboiiii
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -U sciolyid
```

Create token file:

```sh
cp setup.sh.example setup.sh
```

Set your Discord token in `setup.sh`:

```sh
export token="YOUR_DISCORD_BOT_TOKEN"
```

## Redis (macOS recommended)

```sh
brew install redis
brew services start redis
redis-cli ping
```

## Run

```sh
source .venv/bin/activate
source setup.sh
python water_quality_bot.py
```

## Common commands

Using default prefixes in `water_quality_bot.py`:

- `w.e` or `w!e` -> get image
- `w.c <guess>` -> check
- `w.h` -> hint
- `w.sk` -> skip

