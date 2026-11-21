# News in One Image — Saturday 21 November 2026 (v1)

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/wahyunp26-source/news-image-20261121-v1/rank.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/wahyunp26-source/news-image-20261121-v1/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Referral: `amzcd6wq`

A single-day newspaper front page for **Saturday 21 November 2026**: 36
verified stories across 7 regions, in the classic front-page layout — huge
serif date headline, six-number stats strip, region tabs, 3 big features and
10 medium stories, each with its own matching flat-vector illustration, a
world map with 12 numbered pins, 23 more one-line briefs, and a DATE CHECK
that lists the big Friday-first stories left out on purpose.

## What happened that day

- **Kyiv** hit by the war's biggest barrage — 400+ drones, 100+ missiles,
  at least 8 killed, bridges hit.
- **Wall Street enters correction** — S&P −3.7%, Dow −950, Nasdaq −5.3%,
  the worst week since 2020 as the AI rout deepens.
- **COP31** in Antalya goes into overtime as fossil-fuel talks deadlock and
  the draft drops the words "fossil fuels".
- **Cyclone Akvan** makes landfall near Gopalpur, Odisha — 300,000+
  evacuated; **GTA VI** takes $3.79bn on day one; **Nvidia** craters 14%
  as its CEO is ousted; **Starc 7/58** wrecks England for 172 in Perth.

## How it is built

- `main.py` — stdlib-only entrypoint: copies `entry.png` to the output dir.
- `build.py` — build-time compositor (Pillow): lays out the page from the
  illustrations in `assets/` using Liberation Sans / Liberation Serif.
- `assets/` — 13 feature illustrations + 1 world map, all flat-vector style,
  generated for this entry.
- `entry.png` — the finished 1024×1024 page (JPEG bytes, ≤ 1 MiB).

Run: `python3 main.py` (writes `/output/entry.png`; set
`MAKEFUN_OUTPUT_DIR` to change the destination). Run twice — byte-identical.
