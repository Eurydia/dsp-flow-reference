# Magnet

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Smelting/1-1.txt|1-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item         | Ratio |
| --------------- | --------- | ------------ | ----- |
| 1               | Input     | [[Iron Ore]] | 1/1   |
| 2               | Output    | [[Magnet]]   | 1/1   |

### Arc Smelter

The number of **Arc Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720          | 1800          |
| ------------------------ | ----------- | ------------ | ------------- |
| None                     | `9`         | `18`         | `45`          |
| Extra Products +12.5%    | `8`         | `16`         | `40`          |
| Extra Products +20%      | `7 [336.0]` | `15`         | `37 [1776.0]` |
| Extra Products +25%      | `7 [350.0]` | `14 [700.0]` | `36`          |
| Production Speedup +25%  | `7 [350.0]` | `14 [700.0]` | `36`          |
| Production Speedup +50%  | `6`         | `12`         | `30`          |
| Production Speedup +100% | `4 [320.0]` | `9`          | `22 [1760.0]` |

### Plane Smelter

The number of **Plane Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720         | 1800          |
| ------------------------ | ----------- | ----------- | ------------- |
| None                     | `4 [320.0]` | `9`         | `22 [1760.0]` |
| Extra Products +12.5%    | `4`         | `8`         | `20`          |
| Extra Products +20%      | `3 [288.0]` | `7 [672.0]` | `18 [1728.0]` |
| Extra Products +25%      | `3 [300.0]` | `7 [700.0]` | `18`          |
| Production Speedup +25%  | `3 [300.0]` | `7 [700.0]` | `18`          |
| Production Speedup +50%  | `3`         | `6`         | `15`          |
| Production Speedup +100% | `2 [320.0]` | `4 [640.0]` | `11 [1760.0]` |
