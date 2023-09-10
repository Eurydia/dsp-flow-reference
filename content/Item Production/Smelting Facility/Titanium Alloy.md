# Titanium Alloy

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Smelting Facility/Smelting Facility 4I-1O.txt|Smelting Facility 4I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item               | Ratio |
| --------------- | --------- | ------------------ | ----- |
| 1               | Input     | [[Titanium Ingot]] | 4/4   |
| 2               | Input     | [[Steel]]          | 4/4   |
| 3               | Input     | [[Sulfuric Acid]]  | 4/8   |
| 4               | Input     | [[Sulfuric Acid]]  | 4/8   |
| 5               | Output    | [[Titanium Alloy]] | 4/4   |

### Arc Smelter

The number of **Arc Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360          | 720          | 1800 |
| ------------------------ | ------------ | ------------ | ---- |
| None                     | `18`         | `36`         | `90` |
| Extra Products +12.5%    | `16`         | `32`         | `80` |
| Extra Products +20%      | `15`         | `30`         | `75` |
| Extra Products +25%      | `14 [350.0]` | `28 [700.0]` | `72` |
| Production Speedup +25%  | `14 [350.0]` | `28 [700.0]` | `72` |
| Production Speedup +50%  | `12`         | `24`         | `60` |
| Production Speedup +100% | `9`          | `18`         | `45` |

### Plane Smelter

The number of **Plane Smelter** required to satisfy different production targets (items per minute).

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
