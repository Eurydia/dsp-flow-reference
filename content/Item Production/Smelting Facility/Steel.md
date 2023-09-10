# Steel

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Smelting Facility/Smelting Facility 3I-1O.txt|Smelting Facility 3I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item           | Ratio |
| --------------- | --------- | -------------- | ----- |
| 1               | Input     | [[Iron Ingot]] | 1/3   |
| 2               | Input     | [[Iron Ingot]] | 1/3   |
| 3               | Input     | [[Iron Ingot]] | 1/3   |
| 4               | Output    | [[Steel]]      | 1/1   |

### Arc Smelter

The number of **Arc Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                  | 720                   | 1800           |
| ------------------------ | -------------------- | --------------------- | -------------- |
| None                     | `3*6=18`             | `3*12=36`             | `3*30=90`      |
| Extra Products +12.5%    | `(2*6)+4=16`         | `(2*12)+8=32`         | `(2*30)+20=80` |
| Extra Products +20%      | `(2*6)+3=15`         | `(2*12)+6=30`         | `(2*30)+15=75` |
| Extra Products +25%      | `(2*6)+2=14 [350.0]` | `(2*12)+4=28 [700.0]` | `(2*30)+12=72` |
| Production Speedup +25%  | `(3*4)+2=14 [350.0]` | `(3*9)+1=28 [700.0]`  | `3*24=72`      |
| Production Speedup +50%  | `3*4=12`             | `3*8=24`              | `3*20=60`      |
| Production Speedup +100% | `3*3=9`              | `3*6=18`              | `3*15=45`      |

### Plane Smelter

The number of **Plane Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                 | 720                  | 1800                   |
| ------------------------ | ------------------- | -------------------- | ---------------------- |
| None                     | `3*3=9`             | `3*6=18`             | `3*15=45`              |
| Extra Products +12.5%    | `(2*3)+2=8`         | `(2*6)+4=16`         | `(2*15)+10=40`         |
| Extra Products +20%      | `(2*3)+1=7 [336.0]` | `(2*6)+3=15`         | `(2*15)+7=37 [1776.0]` |
| Extra Products +25%      | `(2*3)+1=7 [350.0]` | `(2*6)+2=14 [700.0]` | `(2*15)+6=36`          |
| Production Speedup +25%  | `(3*2)+1=7 [350.0]` | `(3*4)+2=14 [700.0]` | `3*12=36`              |
| Production Speedup +50%  | `3*2=6`             | `3*4=12`             | `3*10=30`              |
| Production Speedup +100% | `4*1=4 [320.0]`     | `3*3=9`              | `(3*7)+1=22 [1760.0]`  |
