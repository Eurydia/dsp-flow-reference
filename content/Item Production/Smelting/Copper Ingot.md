# Copper Ingot

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Smelting/1-1.txt|1-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item             | Ratio |
| --------------- | --------- | ---------------- | ----- |
| 1               | Input     | [[Copper Ore]]   | 1/1   |
| 2               | Output    | [[Copper Ingot]] | 1/1   |

### Arc Smelter

The number of **Arc Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720          | 1800          |
| ------------------------ | ----------- | ------------ | ------------- |
| None                     | `6`         | `12`         | `30`          |
| Extra Products +12.5%    | `5 [337.5]` | `10 [675.0]` | `26 [1755.0]` |
| Extra Products +20%      | `5`         | `10`         | `25`          |
| Extra Products +25%      | `4 [300.0]` | `9 [675.0]`  | `24`          |
| Production Speedup +25%  | `4 [300.0]` | `9 [675.0]`  | `24`          |
| Production Speedup +50%  | `4`         | `8`          | `20`          |
| Production Speedup +100% | `3`         | `6`          | `15`          |

### Plane Smelter

The number of **Plane Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720         | 1800          |
| ------------------------ | ----------- | ----------- | ------------- |
| None                     | `3`         | `6`         | `15`          |
| Extra Products +12.5%    | `2 [270.0]` | `5 [675.0]` | `13 [1755.0]` |
| Extra Products +20%      | `2 [288.0]` | `5`         | `12 [1728.0]` |
| Extra Products +25%      | `2 [300.0]` | `4 [600.0]` | `12`          |
| Production Speedup +25%  | `2 [300.0]` | `4 [600.0]` | `12`          |
| Production Speedup +50%  | `2`         | `4`         | `10`          |
| Production Speedup +100% | `1 [240.0]` | `3`         | `7 [1680.0]`  |
