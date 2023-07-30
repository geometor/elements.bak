from pathlib import Path

p = Path('I/propositions')

for x in p.iterdir():
    if x.is_dir():
        rd = x.parent / x.stem
        x.rename(rd)
