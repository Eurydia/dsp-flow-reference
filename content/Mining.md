# Mining

Nodes:
- [[Iron Ore]]
- [[Copper Ore]]
- [[Stone]]
- [[Coal]]
- [[Silicon Ore]]
- [[Titanium Ore]]
- [[Kimberlite Ore]]
- [[Fractal Silicon]]
- [[Optical Grating Crystal]]
- [[Spiniform Stalagmite Crystal]]
- [[Unipolar Magnet]]

## General Formulas

General formula with **Vein Utilization** for Mining Machines.

$$
\frac{V}{M\cdot\left(1+\frac{k}{10}\right)}
$$

| Symbol | Meaning                                   |
| ------ | ----------------------------------------- |
| $V$    | Target transport volume (item per minute) |
| $M$    | Mining speed (item per minute per node)   |
| $k$    | Vein Utilization level                    |

## Datasheet

Different transport volumes of Conveyor Belts (item per minute).

| Conveyor Belt | Base Volume | Double Cargo Stacking | Triple Cargo Stacking | Quadruple Cargo Stacking |
| ------------- | ----------- | --------------------- | --------------------- | ------------------------ |
| Mk. I         | 360         | 720                   | 1,080                 | 1,440                    |
| Mk. II        | 720         | 1,440                 | 2,160                 | 2,880                    |
| Mk. III       | 1,800       | 3,600                 | 5,400                 | 7,200                    |

Total number of nodes required to fill different setup of **Conveyor Belt Mk. I**.

| Conveyor Belt Mk. I Setup | Mining Machine | Advanced Mining Machine |
| ------------------------- | -------------- | ----------------------- |
| Base Volume               | 12             | 6                       |
| Double Cargo Stacking     | 24             | 12                      |
| Triple Cargo Stacking     | 36             | 18                      |
| Quadruple Cargo Stacking  | 48             | 24                      |

Total number of nodes required to fill different setup of **Conveyor Belt Mk. II**.

| Conveyor Belt Mk. II Setup | Mining Machine | Advanced Mining Machine |
| -------------------------- | -------------- | ----------------------- |
| Base Volume                | 24             | 12                      |
| Double Cargo Stacking      | 48             | 24                      |
| Triple Cargo Stacking      | 72             | 36                      |
| Quadruple Cargo Stacking   | 96             | 48                      |

Total number of nodes required to fill different setups of **Conveyor Belt Mk. III**.

| Conveyor Belt Mk. III Setup | Mining Machine | Advanced Mining Machine |
| --------------------------- | -------------- | ----------------------- |
| Base Volume                 | 60             | 30                      |
| Double Cargo Stacking       | 120            | 60                      |
| Triple Cargo Stacking       | 180            | 90                      |
| Quadruple Cargo Stacking    | 240            | 120                     |
