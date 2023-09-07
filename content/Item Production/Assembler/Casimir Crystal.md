# Casimir Crystal

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/5-1.txt|5-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                 | Ratio |
| --------------- | --------- | -------------------- | ----- |
| 1               | Input     | [[Titanium Crystal]] | 1/1   |
| 2               | Input     | [[Graphene]]         | 2/2   |
| 3               | Input     | [[Hydrogen]]         | 4/12  |
| 4               | Input     | [[Hydrogen]]         | 4/12  |
| 5               | Input     | [[Hydrogen]]         | 4/12  |
| 6               | Output    | [[Casimir Crystal]]  | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `4*8=32`              | `4*16=64`              | `4*40=160`                |
| Extra Products +12.5%    | `(3*8)+4=28 [354.38]` | `(3*16)+8=56 [708.75]` | `(3*40)+22=142 [1797.19]` |
| Extra Products +20%      | `(3*8)+2=26 [351.0]`  | `(3*16)+5=53 [715.5]`  | `(3*40)+13=133 [1795.5]`  |
| Extra Products +25%      | `(3*8)+1=25 [351.56]` | `(3*16)+3=51 [717.19]` | `(3*40)+8=128`            |
| Production Speedup +25%  | `(4*6)+1=25 [351.56]` | `(4*12)+3=51 [717.19]` | `4*32=128`                |
| Production Speedup +50%  | `(4*5)+1=21 [354.38]` | `(4*10)+2=42 [708.75]` | `(4*26)+2=106 [1788.75]`  |
| Production Speedup +100% | `4*4=16`              | `4*8=32`               | `4*20=80`                 |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `4*6=24`              | `4*12=48`              | `4*30=120`                |
| Extra Products +12.5%    | `(3*6)+3=21 [354.38]` | `(3*12)+6=42 [708.75]` | `(3*30)+16=106 [1788.75]` |
| Extra Products +20%      | `(3*6)+2=20`          | `(3*12)+4=40`          | `(3*30)+10=100`           |
| Extra Products +25%      | `(3*6)+1=19 [356.25]` | `(3*12)+2=38 [712.5]`  | `(3*30)+6=96`             |
| Production Speedup +25%  | `(4*4)+3=19 [356.25]` | `(4*9)+2=38 [712.5]`   | `4*24=96`                 |
| Production Speedup +50%  | `4*4=16`              | `4*8=32`               | `4*20=80`                 |
| Production Speedup +100% | `4*3=12`              | `4*6=24`               | `4*15=60`                 |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                   | 1800                     |
| ------------------------ | --------------------- | --------------------- | ------------------------ |
| None                     | `4*4=16`              | `4*8=32`              | `4*20=80`                |
| Extra Products +12.5%    | `(3*4)+2=14 [354.38]` | `(3*8)+4=28 [708.75]` | `(3*20)+11=71 [1797.19]` |
| Extra Products +20%      | `(3*4)+1=13 [351.0]`  | `(3*8)+2=26 [702.0]`  | `(3*20)+6=66 [1782.0]`   |
| Extra Products +25%      | `3*4=12 [337.5]`      | `(3*8)+1=25 [703.12]` | `(3*20)+4=64`            |
| Production Speedup +25%  | `4*3=12 [337.5]`      | `(4*6)+1=25 [703.12]` | `4*16=64`                |
| Production Speedup +50%  | `5*2=10 [337.5]`      | `(4*5)+1=21 [708.75]` | `(4*13)+1=53 [1788.75]`  |
| Production Speedup +100% | `4*2=8`               | `4*4=16`              | `4*10=40`                |