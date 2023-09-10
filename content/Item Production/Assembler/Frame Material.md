# Frame Material

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/Assembler 4I-1O.txt|Assembler 4I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                    | Ratio |
| --------------- | --------- | ----------------------- | ----- |
| 1               | Input     | [[High-Purity Silicon]] | 1/1   |
| 2               | Input     | [[Titanium Ingot]]      | 1/1   |
| 3               | Input     | [[Carbon Nanotube]]     | 2/4   |
| 4               | Input     | [[Carbon Nanotube]]     | 2/4   |
| 5               | Output    | [[Frame Material]]      | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                     | 720                     | 1800                       |
| ------------------------ | ----------------------- | ----------------------- | -------------------------- |
| None                     | `2*24=48`               | `2*48=96`               | `2*120=240`                |
| Extra Products +12.5%    | `(1*24)+18=42 [354.38]` | `(1*48)+37=85 [717.19]` | `(1*120)+93=213 [1797.19]` |
| Extra Products +20%      | `(1*24)+16=40`          | `(1*48)+32=80`          | `(1*120)+80=200`           |
| Extra Products +25%      | `(1*24)+14=38 [356.25]` | `(1*48)+28=76 [712.5]`  | `(1*120)+72=192`           |
| Production Speedup +25%  | `2*19=38 [356.25]`      | `2*38=76 [712.5]`       | `2*96=192`                 |
| Production Speedup +50%  | `2*16=32`               | `2*32=64`               | `2*80=160`                 |
| Production Speedup +100% | `2*12=24`               | `2*24=48`               | `2*60=120`                 |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                    | 720                    | 1800            |
| ------------------------ | ---------------------- | ---------------------- | --------------- |
| None                     | `2*18=36`              | `2*36=72`              | `2*90=180`      |
| Extra Products +12.5%    | `(1*18)+14=32`         | `(1*36)+28=64`         | `(1*90)+70=160` |
| Extra Products +20%      | `(1*18)+12=30`         | `(1*36)+24=60`         | `(1*90)+60=150` |
| Extra Products +25%      | `(1*18)+10=28 [350.0]` | `(1*36)+21=57 [712.5]` | `(1*90)+54=144` |
| Production Speedup +25%  | `2*14=28 [350.0]`      | `(2*28)+1=57 [712.5]`  | `2*72=144`      |
| Production Speedup +50%  | `2*12=24`              | `2*24=48`              | `2*60=120`      |
| Production Speedup +100% | `2*9=18`               | `2*18=36`              | `2*45=90`       |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                    | 720                     | 1800                      |
| ------------------------ | ---------------------- | ----------------------- | ------------------------- |
| None                     | `2*12=24`              | `2*24=48`               | `2*60=120`                |
| Extra Products +12.5%    | `(1*12)+9=21 [354.38]` | `(1*24)+18=42 [708.75]` | `(1*60)+46=106 [1788.75]` |
| Extra Products +20%      | `(1*12)+8=20`          | `(1*24)+16=40`          | `(1*60)+40=100`           |
| Extra Products +25%      | `(1*12)+7=19 [356.25]` | `(1*24)+14=38 [712.5]`  | `(1*60)+36=96`            |
| Production Speedup +25%  | `(2*9)+1=19 [356.25]`  | `2*19=38 [712.5]`       | `2*48=96`                 |
| Production Speedup +50%  | `2*8=16`               | `2*16=32`               | `2*40=80`                 |
| Production Speedup +100% | `2*6=12`               | `2*12=24`               | `2*30=60`                 |
