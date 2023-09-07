# Plasma Exciter

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/3-1.txt|3-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item               | Ratio |
| --------------- | --------- | ------------------ | ----- |
| 1               | Input     | [[Prism]]          | 2/2   |
| 2               | Input     | [[Magnetic Coil]]  | 2/4   |
| 3               | Input     | [[Magnetic Coil]]  | 2/4   |
| 4               | Output    | [[Plasma Exciter]] | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

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

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                  | 720                    | 1800                     |
| ------------------------ | -------------------- | ---------------------- | ------------------------ |
| None                     | `2*6=12`             | `2*12=24`              | `2*30=60`                |
| Extra Products +12.5%    | `(1*6)+4=10 [337.5]` | `(1*12)+9=21 [708.75]` | `(1*30)+23=53 [1788.75]` |
| Extra Products +20%      | `(1*6)+4=10`         | `(1*12)+8=20`          | `(1*30)+20=50`           |
| Extra Products +25%      | `(1*6)+3=9 [337.5]`  | `(1*12)+7=19 [712.5]`  | `(1*30)+18=48`           |
| Production Speedup +25%  | `(2*4)+1=9 [337.5]`  | `(2*9)+1=19 [712.5]`   | `2*24=48`                |
| Production Speedup +50%  | `2*4=8`              | `2*8=16`               | `2*20=40`                |
| Production Speedup +100% | `2*3=6`              | `2*6=12`               | `2*15=30`                |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                  | 720                   | 1800                     |
| ------------------------ | -------------------- | --------------------- | ------------------------ |
| None                     | `2*4=8`              | `2*8=16`              | `2*20=40`                |
| Extra Products +12.5%    | `(1*4)+3=7 [354.38]` | `(1*8)+6=14 [708.75]` | `(1*20)+15=35 [1771.88]` |
| Extra Products +20%      | `(1*4)+2=6 [324.0]`  | `(1*8)+5=13 [702.0]`  | `(1*20)+13=33 [1782.0]`  |
| Extra Products +25%      | `(1*4)+2=6 [337.5]`  | `(1*8)+4=12 [675.0]`  | `(1*20)+12=32`           |
| Production Speedup +25%  | `2*3=6 [337.5]`      | `2*6=12 [675.0]`      | `2*16=32`                |
| Production Speedup +50%  | `(2*2)+1=5 [337.5]`  | `2*5=10 [675.0]`      | `2*13=26 [1755.0]`       |
| Production Speedup +100% | `2*2=4`              | `2*4=8`               | `2*10=20`                |