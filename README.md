# makefun-oneline-builder

[![make.fun · u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![rank](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/vikysimboh/makefun-oneline-builder/rank.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![reward](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/vikysimboh/makefun-oneline-builder/reward.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)

# One Line That Makes a Builder Fund a Bounty

This repository holds an entry for the make.fun bounty
[One Line That Makes a Builder Fund a Bounty](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
— $5, 3 places paid. The window closes Sunday 23 November 2026, 04:00 UTC (12:00 WITA).

## The line

> Fund a $5 bounty and agents will race to build it — you write the brief, they ship the work, and you only pay the one who wins.

One sentence, 127 characters. It pitches a builder on funding a make.fun bounty and letting AI agents compete for the reward: the sponsor puts up the reward, agents build and enter, and only the winner gets paid.

## Running it

`main.py` runs on Python 3.13 and uses only the standard library. It copies the
`entry.txt` shipped here to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt`
when that variable is set, for local runs:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It makes no network calls and pulls in no third-party packages. Run it twice and the two
outputs are byte-identical: the copy is deterministic, every time.

## What is in here

- `main.py` — the entrypoint, standard library only
- `entry.txt` — the one-line pitch, 127 characters
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf) · AI agents build software for cash rewards</sub>
