# Antimatter Fuel Rod

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/Assembler 4I-1O.txt|Assembler 4I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                               | Ratio |
| --------------- | --------- | ---------------------------------- | ----- |
| 1               | Input     | [[Titanium Alloy]]                 | 1/1   |
| 2               | Input     | [[Annihilation Constraint Sphere]] | 1/1   |
| 3               | Input     | [[Hydrogen]]                       | 12/12 |
| 4               | Input     | [[Antimatter]]                     | 12/12 |
| 5               | Output    | [[Deuteron Fuel Rod]]              | 2/2   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                    | 720                     | 1800           |
| ------------------------ | ---------------------- | ----------------------- | -------------- |
| None                     | `6*16=96`              | `6*32=192`              | `6*80=480`     |
| Production Speedup +25%  | `(6*12)+4=76 [356.25]` | `(6*25)+3=153 [717.19]` | `6*64=384`     |
| Production Speedup +50%  | `(6*10)+4=64`          | `(6*21)+2=128`          | `(6*53)+2=320` |
| Production Speedup +100% | `6*8=48`               | `6*16=96`               | `6*40=240`     |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                     | 1800       |
| ------------------------ | --------------------- | ----------------------- | ---------- |
| None                     | `6*12=72`             | `6*24=144`              | `6*60=360` |
| Production Speedup +25%  | `(6*9)+3=57 [356.25]` | `(6*19)+1=115 [718.75]` | `6*48=288` |
| Production Speedup +50%  | `6*8=48`              | `6*16=96`               | `6*40=240` |
| Production Speedup +100% | `6*6=36`              | `6*12=72`               | `6*30=180` |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                   | 1800           |
| ------------------------ | --------------------- | --------------------- | -------------- |
| None                     | `6*8=48`              | `6*16=96`             | `6*40=240`     |
| Production Speedup +25%  | `(6*6)+2=38 [356.25]` | `(6*12)+4=76 [712.5]` | `6*32=192`     |
| Production Speedup +50%  | `(6*5)+2=32`          | `(6*10)+4=64`         | `(6*26)+4=160` |
| Production Speedup +100% | `6*4=24`              | `6*8=48`              | `6*20=120`     |
