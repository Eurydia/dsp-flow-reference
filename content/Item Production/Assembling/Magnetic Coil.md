# Magnetic Coil

## Blueprints

**Recommended standard blueprints**: [[content/Standard Set/Blueprints/Assembling Machine/3-1.txt|3-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item              |
| --------------- | --------- | ----------------- |
| 1               | Input     | [[Magnet]] (1/2)  |
| 2               | Input     | [[Magnet]] (1/2)  | 
| 3               | Input     | [[Copper Ingot]]  |
| 4               | Output    | [[Circuit Board]] |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

| Proliferation            | 360         | 720         | 1800         |
| ------------------------ | ----------- | ----------- | ------------ |
| None                     | `2*2=4`     | `2*4=8`     | `2*10=20`    |
| Extra Products +12.5%    | `2*2=4`     | `2*4=8`     | `2*9=18`     | 
| Extra Products +20%      | `2*2=4`     | `(1*4)+3=7` | `(1*9)+8=17` |
| Extra Products +25%      | `2*2=4`     | `(1*4)+3=7` | `2*8=16`     |
| Production Speedup +25%  | `2*2=4`     | `(1*4)+3=7` | `2*8=16`     |
| Production Speedup +50%  | `(1*2)+1=3` | `2*3=6`     | `2*7=14`     |
| Production Speedup +100% | `2*1=2`     | `2*2=4`     | `2*5=10`     |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

| Proliferation            | 360         | 720         | 1800         |
| ------------------------ | ----------- | ----------- | ------------ |
| None                     | `(1*2)+1=3` | `2*3=6`     | `(1*8)+7=15` |
| Extra Products +12.5%    | `(1*2)+1=3` | `2*3=6`     | `2*7=14`     |
| Extra Products +20%      | `(1*2)+1=3` | `(1*3)+2=5` | `(1*7)+6=13` |
| Extra Products +25%      | `(1*2)+1=3` | `(1*3)+2=5` | `2*6=12`     |
| Production Speedup +25%  | `(1*2)+1=3` | `(1*3)+2=5` | `2*6=12`     |
| Production Speedup +50%  | `2*1=2`     | `2*2=4`     | `2*5=10`     |
| Production Speedup +100% | `2*1=2`     | `(1*2)+1=3` | `2*4=8`      |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

| Proliferation            | 360     | 720         | 1800        |
| ------------------------ | ------- | ----------- | ----------- |
| None                     | `2*1=2` | `2*2=4`     | `2*5=10`    |
| Extra Products +12.5%    | `2*1=2` | `2*2=4`     | `(1*5)+4=9` |
| Extra Products +20%      | `2*1=2` | `2*2=4`     | `(1*5)+4=9` |
| Extra Products +25%      | `2*1=2` | `2*2=4`     | `2*4=8`     |
| Production Speedup +25%  | `2*1=2` | `2*2=4`     | `2*4=8`     |
| Production Speedup +50%  | `2*1=2` | `(1*2)+1=3` | `(1*4)+3=7` |
| Production Speedup +100% | `1`     | `2*1=2`     | `(1*3)+2=5` |

