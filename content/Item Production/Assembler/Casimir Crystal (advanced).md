# Casimir Crystal (advanced)

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/Assembler 5I-1O.txt|Assembler 5I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                        | Ratio |
| --------------- | --------- | --------------------------- | ----- |
| 1               | Input     | [[Graphene]]                | 2/2   |
| 2               | Input     | [[Optical Grating Crystal]] | 4/8   |
| 3               | Input     | [[Optical Grating Crystal]] | 4/8   |
| 4               | Input     | [[Hydrogen]]                | 6/12  |
| 5               | Input     | [[Hydrogen]]                | 6/12  |
| 6               | Output    | [[Casimir Crystal]]         | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `(6*5)+2=32`          | `(6*10)+4=64`          | `(6*26)+4=160`            |
| Extra Products +12.5%    | `(5*5)+3=28 [354.38]` | `(5*10)+6=56 [708.75]` | `(5*26)+12=142 [1797.19]` |
| Extra Products +20%      | `(5*5)+1=26 [351.0]`  | `(5*10)+3=53 [715.5]`  | `(5*26)+3=133 [1795.5]`   |
| Extra Products +25%      | `5*5=25 [351.56]`     | `(5*10)+1=51 [717.19]` | `(4*26)+24=128`           |
| Production Speedup +25%  | `(6*4)+1=25 [351.56]` | `(6*8)+3=51 [717.19]`  | `(6*21)+2=128`            |
| Production Speedup +50%  | `7*3=21 [354.38]`     | `6*7=42 [708.75]`      | `(6*17)+4=106 [1788.75]`  |
| Production Speedup +100% | `8*2=16`              | `(6*5)+2=32`           | `(6*13)+2=80`             |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                   | 1800                     |
| ------------------------ | --------------------- | --------------------- | ------------------------ |
| None                     | `6*4=24`              | `6*8=48`              | `6*20=120`               |
| Extra Products +12.5%    | `(5*4)+1=21 [354.38]` | `(5*8)+2=42 [708.75]` | `(5*20)+6=106 [1788.75]` |
| Extra Products +20%      | `5*4=20`              | `5*8=40`              | `5*20=100`               |
| Extra Products +25%      | `(4*4)+3=19 [356.25]` | `(4*8)+6=38 [712.5]`  | `(4*20)+16=96`           |
| Production Speedup +25%  | `(6*3)+1=19 [356.25]` | `(6*6)+2=38 [712.5]`  | `6*16=96`                |
| Production Speedup +50%  | `8*2=16`              | `(6*5)+2=32`          | `(6*13)+2=80`            |
| Production Speedup +100% | `6*2=12`              | `6*4=24`              | `6*10=60`                |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                  | 720                   | 1800                    |
| ------------------------ | -------------------- | --------------------- | ----------------------- |
| None                     | `8*2=16`             | `(6*5)+2=32`          | `(6*13)+2=80`           |
| Extra Products +12.5%    | `7*2=14 [354.38]`    | `(5*5)+3=28 [708.75]` | `(5*13)+6=71 [1797.19]` |
| Extra Products +20%      | `(6*2)+1=13 [351.0]` | `(5*5)+1=26 [702.0]`  | `(5*13)+1=66 [1782.0]`  |
| Extra Products +25%      | `6*2=12 [337.5]`     | `5*5=25 [703.12]`     | `(4*13)+12=64`          |
| Production Speedup +25%  | `6*2=12 [337.5]`     | `(6*4)+1=25 [703.12]` | `(6*10)+4=64`           |
| Production Speedup +50%  | `10*1=10 [337.5]`    | `7*3=21 [708.75]`     | `(6*8)+5=53 [1788.75]`  |
| Production Speedup +100% | `8*1=8`              | `8*2=16`              | `(6*6)+4=40`            |
