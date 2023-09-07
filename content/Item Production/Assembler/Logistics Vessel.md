# Logistics Vessel

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/5-1.txt|5-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                    | Ratio |
| --------------- | --------- | ----------------------- | ----- |
| 1               | Input     | [[Titanium Alloy]]      | 5/10  |
| 2               | Input     | [[Titanium Alloy]]      | 5/10  |
| 3               | Input     | [[Processor]]           | 5/10  |
| 4               | Input     | [[Processor]]           | 5/10  |
| 5               | Input     | [[Reinforced Thruster]] | 2/2   |
| 6               | Output    | [[Logistics Vessel]]    | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `(5*9)+3=48`          | `(5*19)+1=96`          | `5*48=240`                |
| Extra Products +12.5%    | `(4*9)+6=42 [354.38]` | `(4*19)+9=85 [717.19]` | `(4*48)+21=213 [1797.19]` |
| Extra Products +20%      | `(4*9)+4=40`          | `(4*19)+4=80`          | `(4*48)+8=200`            |
| Extra Products +25%      | `(4*9)+2=38 [356.25]` | `4*19=76 [712.5]`      | `4*48=192`                |
| Production Speedup +25%  | `(5*7)+3=38 [356.25]` | `(5*15)+1=76 [712.5]`  | `(5*38)+2=192`            |
| Production Speedup +50%  | `(5*6)+2=32`          | `(5*12)+4=64`          | `5*32=160`                |
| Production Speedup +100% | `6*4=24`              | `(5*9)+3=48`           | `5*24=120`                |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                  | 720                   | 1800            |
| ------------------------ | -------------------- | --------------------- | --------------- |
| None                     | `(5*7)+1=36`         | `(5*14)+2=72`         | `5*36=180`      |
| Extra Products +12.5%    | `(4*7)+4=32`         | `(4*14)+8=64`         | `(4*36)+16=160` |
| Extra Products +20%      | `(4*7)+2=30`         | `(4*14)+4=60`         | `(4*36)+6=150`  |
| Extra Products +25%      | `4*7=28 [350.0]`     | `(4*14)+1=57 [712.5]` | `4*36=144`      |
| Production Speedup +25%  | `(5*5)+3=28 [350.0]` | `(5*11)+2=57 [712.5]` | `(5*28)+4=144`  |
| Production Speedup +50%  | `6*4=24`             | `(5*9)+3=48`          | `5*24=120`      |
| Production Speedup +100% | `6*3=18`             | `(5*7)+1=36`          | `5*18=90`       |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                   | 1800                      |
| ------------------------ | --------------------- | --------------------- | ------------------------- |
| None                     | `6*4=24`              | `(5*9)+3=48`          | `5*24=120`                |
| Extra Products +12.5%    | `(5*4)+1=21 [354.38]` | `(4*9)+6=42 [708.75]` | `(4*24)+10=106 [1788.75]` |
| Extra Products +20%      | `5*4=20`              | `(4*9)+4=40`          | `(4*24)+4=100`            |
| Extra Products +25%      | `(4*4)+3=19 [356.25]` | `(4*9)+2=38 [712.5]`  | `4*24=96`                 |
| Production Speedup +25%  | `(6*3)+1=19 [356.25]` | `(5*7)+3=38 [712.5]`  | `(5*19)+1=96`             |
| Production Speedup +50%  | `(5*3)+1=16`          | `(5*6)+2=32`          | `5*16=80`                 |
| Production Speedup +100% | `6*2=12`              | `6*4=24`              | `5*12=60`                 |