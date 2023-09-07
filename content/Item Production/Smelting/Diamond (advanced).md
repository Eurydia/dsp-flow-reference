# Diamond (advanced)

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Smelting/1-1.txt|1-1]]

**Item transportation table**

| Conveyor Belt # | Direction | Item               | Ratio |
| --------------- | --------- | ------------------ | ----- |
| 1               | Input     | [[Kimberlite Ore]] | 1/1   |
| 2               | Output    | [[Diamond]]        | 2/2   |

### Arc Smelter

The number of **Arc Smelter** required to satisfy different production targets (items per minute).

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

### Plane Smelter

The number of **Plane Smelter** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720         | 1800          |
| ------------------------ | ----------- | ----------- | ------------- |
| None                     | `2 [320.0]` | `4 [640.0]` | `11 [1760.0]` |
| Extra Products +12.5%    | `2`         | `4`         | `10`          |
| Extra Products +20%      | `1 [192.0]` | `3 [576.0]` | `9 [1728.0]`  |
| Extra Products +25%      | `1 [200.0]` | `3 [600.0]` | `9`           |
| Production Speedup +25%  | `1 [200.0]` | `3 [600.0]` | `9`           |
| Production Speedup +50%  | `1 [240.0]` | `3`         | `7 [1680.0]`  |
| Production Speedup +100% | `1 [320.0]` | `2 [640.0]` | `5 [1600.0]`  |
