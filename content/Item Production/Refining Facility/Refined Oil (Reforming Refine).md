# Refined Oil (Reforming Refine)

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Refining Facility/Refining Facility 3I-1O.txt|Refining Facility 3I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item            | Ratio |
| --------------- | --------- | --------------- | ----- |
| 1               | Input     | [[Hydrogen]]    | 1/1   |
| 2               | Input     | [[Coal]]        | 1/1   |
| 3               | Input     | [[Refined Oil]] | 2/2   |
| 4               | Output    | [[Refined Oil]] | 3/3   |

### Oil Refinery

The number of **Oil Refinery** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360         | 720          | 1800          |
| ------------------------ | ----------- | ------------ | ------------- |
| None                     | `8`         | `16`         | `40`          |
| Production Speedup +25%  | `6 [337.5]` | `12 [675.0]` | `32`          |
| Production Speedup +50%  | `5 [337.5]` | `10 [675.0]` | `26 [1755.0]` |
| Production Speedup +100% | `4`         | `8`          | `20`          |
