# SOLARLUX — The Catalogue Photo of an Impossible Gadget

[![make.fun](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![Rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/adhais23/solar-flashlight-catalogue/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![Reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/adhais23/solar-flashlight-catalogue/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)

A [make.fun](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341) entry:
a program that writes one catalogue photograph of an impossible gadget
to `/output/entry.png`.

## The gadget

**SOLARLUX — the solar-powered flashlight.** A sleek matte-black torch
with a glossy blue solar panel built into the head of the torch, switched
ON in bright studio light. It only works in sunlight — so its exactly one
accessory is a pair of black sunglasses, lying beside it. The joke reads
at a glance: you need sun (and shades) to use a flashlight.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled studio photograph `photo.png` (1024×1024 PNG, 362,267 bytes)
to `/output/entry.png` and leaves it world-readable.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `photo.png` — the catalogue photograph it writes
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
