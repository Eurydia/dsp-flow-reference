# Particle Container

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/3-1.txt|3-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                        | Ratio |
| --------------- | --------- | --------------------------- | ----- |
| 1               | Input     | [[Electromagnetic Turbine]] | 2/2   |
| 2               | Input     | [[Graphene]]                | 2/2   |
| 3               | Input     | [[Copper Ingot]]            | 2/2   |
| 4               | Output    | [[Particle Container]]      | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                     | 720                     | 1800                      |
| ------------------------ | ----------------------- | ----------------------- | ------------------------- |
| None                     | `2*16=32`               | `2*32=64`               | `2*80=160`                |
| Extra Products +12.5%    | `(1*16)+12=28 [354.38]` | `(1*32)+24=56 [708.75]` | `(1*80)+62=142 [1797.19]` |
| Extra Products +20%      | `(1*16)+10=26 [351.0]`  | `(1*32)+21=53 [715.5]`  | `(1*80)+53=133 [1795.5]`  |
| Extra Products +25%      | `(1*16)+9=25 [351.56]`  | `(1*32)+19=51 [717.19]` | `(1*80)+48=128`           |
| Production Speedup +25%  | `(2*12)+1=25 [351.56]`  | `(2*25)+1=51 [717.19]`  | `2*64=128`                |
| Production Speedup +50%  | `(2*10)+1=21 [354.38]`  | `2*21=42 [708.75]`      | `2*53=106 [1788.75]`      |
| Production Speedup +100% | `2*8=16`                | `2*16=32`               | `2*40=80`                 |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

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

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                     | 1800                     |
| ------------------------ | --------------------- | ----------------------- | ------------------------ |
| None                     | `2*8=16`              | `2*16=32`               | `2*40=80`                |
| Extra Products +12.5%    | `(1*8)+6=14 [354.38]` | `(1*16)+12=28 [708.75]` | `(1*40)+31=71 [1797.19]` |
| Extra Products +20%      | `(1*8)+5=13 [351.0]`  | `(1*16)+10=26 [702.0]`  | `(1*40)+26=66 [1782.0]`  |
| Extra Products +25%      | `(1*8)+4=12 [337.5]`  | `(1*16)+9=25 [703.12]`  | `(1*40)+24=64`           |
| Production Speedup +25%  | `2*6=12 [337.5]`      | `(2*12)+1=25 [703.12]`  | `2*32=64`                |
| Production Speedup +50%  | `2*5=10 [337.5]`      | `(2*10)+1=21 [708.75]`  | `(2*26)+1=53 [1788.75]`  |
| Production Speedup +100% | `2*4=8`               | `2*8=16`                | `2*20=40`                |