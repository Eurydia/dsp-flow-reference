# Particle Container (advanced)

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/3-1.txt|3-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                   | Ratio |
| --------------- | --------- | ---------------------- | ----- |
| 1               | Input     | [[Copper Ingot]]       | 2/2   |
| 2               | Input     | [[Unipolar Magnet]]    | 5/10  |
| 3               | Input     | [[Unipolar Magnet]]    | 5/10  |
| 4               | Output    | [[Particle Container]] | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `(5*6)+2=32`          | `(5*12)+4=64`          | `5*32=160`                |
| Extra Products +12.5%    | `(4*6)+4=28 [354.38]` | `(4*12)+8=56 [708.75]` | `(4*32)+14=142 [1797.19]` |
| Extra Products +20%      | `(4*6)+2=26 [351.0]`  | `(4*12)+5=53 [715.5]`  | `(4*32)+5=133 [1795.5]`   |
| Extra Products +25%      | `(4*6)+1=25 [351.56]` | `(4*12)+3=51 [717.19]` | `4*32=128`                |
| Production Speedup +25%  | `5*5=25 [351.56]`     | `(5*10)+1=51 [717.19]` | `(5*25)+3=128`            |
| Production Speedup +50%  | `(5*4)+1=21 [354.38]` | `(5*8)+2=42 [708.75]`  | `(5*21)+1=106 [1788.75]`  |
| Production Speedup +100% | `(5*3)+1=16`          | `(5*6)+2=32`           | `5*16=80`                 |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

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

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720                   | 1800                    |
| ------------------------ | --------------------- | --------------------- | ----------------------- |
| None                     | `(5*3)+1=16`          | `(5*6)+2=32`          | `5*16=80`               |
| Extra Products +12.5%    | `(4*3)+2=14 [354.38]` | `(4*6)+4=28 [708.75]` | `(4*16)+7=71 [1797.19]` |
| Extra Products +20%      | `(4*3)+1=13 [351.0]`  | `(4*6)+2=26 [702.0]`  | `(4*16)+2=66 [1782.0]`  |
| Extra Products +25%      | `4*3=12 [337.5]`      | `(4*6)+1=25 [703.12]` | `4*16=64`               |
| Production Speedup +25%  | `6*2=12 [337.5]`      | `5*5=25 [703.12]`     | `(5*12)+4=64`           |
| Production Speedup +50%  | `5*2=10 [337.5]`      | `(5*4)+1=21 [708.75]` | `(5*10)+3=53 [1788.75]` |
| Production Speedup +100% | `8*1=8`               | `(5*3)+1=16`          | `5*8=40`                |