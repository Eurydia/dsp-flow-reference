# Particle Container (advanced)

## Blueprints

**Recommended standard blueprints**: [[content/Standard Set/Blueprints/Assembling Machine/5-1.txt|5-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                       |
| --------------- | --------- | -------------------------- |
| 1               | Input     | [[Copper Ingot]]           |
| 2               | Input     | [[Unipolar Magnet]] (5/10) |
| 3               | Input     | [[Unipolar Magnet]] (5/10) |
| 4               | Output    | [[Particle Container]]     | 

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

| Proliferation            | 360          | 720            | 1800            |
| ------------------------ | ------------ | -------------- | --------------- |
| None                     | `(4*7)+4=32` | `(4*13)+12=64` | `5*32=160`      |
| Extra Products +12.5%    | `(4*6)+5=29` | `(4*12)+9=57`  | `(4*29)+27=143` |
| Extra Products +20%      | `(4*6)+3=27` | `(4*11)+10=54` | `(4*27)+26=134` |
| Extra Products +25%      | `(4*6)+2=26` | `(4*11)+8=52`  | `(4*26)+24=128` |
| Production Speedup +25%  | `(4*6)+2=26` | `(4*11)+8=52`  | `(4*26)+24=128` |
| Production Speedup +50%  | `(4*5)+2=22` | `(4*9)+7=43`   | `(4*22)+19=107` |
| Production Speedup +100% | `4*4=16`     | `(4*7)+4=32`   | `5*16=80`       |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

| Proliferation            | 360          | 720           | 1800            |
| ------------------------ | ------------ | ------------- | --------------- |
| None                     | `(4*5)+4=24` | `(4*10)+8=48` | `5*24=120`      |
| Extra Products +12.5%    | `(4*5)+2=22` | `(4*9)+7=43`  | `(4*22)+19=107` |
| Extra Products +20%      | `5*4=20`     | `5*8=40`      | `5*20=100`      |
| Extra Products +25%      | `5*4=20`     | `(4*8)+7=39`  | `(4*20)+16=96`  |
| Production Speedup +25%  | `5*4=20`     | `(4*8)+7=39`  | `(4*20)+16=96`  |
| Production Speedup +50%  | `4*4=16`     | `(4*7)+4=32`  | `5*16=80`       |
| Production Speedup +100% | `4*3=12`     | `(4*5)+4=24`  | `5*12=60`       |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

| Proliferation            | 360          | 720          | 1800           |
| ------------------------ | ------------ | ------------ | -------------- |
| None                     | `4*4=16`     | `(4*7)+4=32` | `5*16=80`      |
| Extra Products +12.5%    | `5*3=15`     | `(4*6)+5=29` | `(4*15)+12=72` |
| Extra Products +20%      | `(4*3)+2=14` | `(4*6)+3=27` | `(4*14)+11=67` |
| Extra Products +25%      | `(4*3)+1=13` | `(4*6)+2=26` | `(4*13)+12=64` |
| Production Speedup +25%  | `(4*3)+1=13` | `(4*6)+2=26` | `(4*13)+12=64` |
| Production Speedup +50%  | `(3*3)+2=11` | `(4*5)+2=22` | `(4*11)+10=54` |
| Production Speedup +100% | `4*2=8`      | `4*4=16`     | `5*8=40`       |

