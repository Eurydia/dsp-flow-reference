# Energetic Graphite (X-Ray Cracking)

## Blueprint

**Recommended standard blueprints**: [[content/Standard Set/Blueprints/Refining/2-4.txt|2-4]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                   | Ratio |
| --------------- | --------- | ---------------------- | ----- |
| 1               | Input     | [[Refined Oil]]        | 1/1   |
| 2               | Input     | [[Hydrogen]]           | 2/2   |
| 3               | Output    | [[Energetic Graphite]] | 1/1   |
| 4               | Output    | [[Refined Oil]]        | 1/3   |
| 5               | Output    | [[Refined Oil]]        | 1/3   |
| 6               | Output    | [[Refined Oil]]        | 1/3   |

### Oil Refinery

The number of **Oil Refinery** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                   | 720               | 1800       |
| ------------------------ | --------------------- | ----------------- | ---------- |
| None                     | `2*12=24`             | `2*24=48`         | `2*60=120` |
| Production Speedup +25%  | `(2*9)+1=19 [356.25]` | `2*19=38 [712.5]` | `2*48=96`  |
| Production Speedup +50%  | `2*8=16`              | `2*16=32`         | `2*40=80`  |
| Production Speedup +100% | `2*6=12`              | `2*12=24`         | `2*30=60`  |
