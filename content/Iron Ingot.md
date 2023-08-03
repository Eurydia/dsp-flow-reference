# Mining Machine 

## General Information

Crafting recipe:

| Items              | Ratio |
| ------------------ | ----- |
| [[Iron Ore]]       | 1     |
| >>> [[Iron Ingot]] | 1     |

Craft in:
- [[Assembling Machine Mk. I]]
- [[Assembling Machine Mk. II]]
- [[Assembling Machine Mk. III]]

Energy consumption:

|                  | Consumption (kW) |
| ---------------- | ---------------- |
| Work consumption | 420              |
| Idle consumption | 24               |

##  Gathering


Mining Machines gather:
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

The base gathering speed is 30 items per node per minute.

Different transport volumes of conveyor belts (item per minute).

| Conveyor Belt | Base Volume | Double Cargo Stacking | Triple Cargo Stacking | Quadruple Cargo Stacking |
| ------------- | ----------- | --------------------- | --------------------- | ------------------------ |
| Mk. I         | 360         | 720                   | 1,080                 | 1,440                    |
| Mk. II        | 720         | 1,440                 | 2,160                 | 2,880                    |
| Mk. III       | 1,800       | 3,600                 | 5,400                 | 7,200                    |

Total number of nodes required for different setup of **Conveyor Belt Mk. I**.

| Conveyor Belt Mk. I Setup | Number of Nodes |
| ------------------------- | --------------- |
| Base Volume               | 12              |
| Double Cargo Stacking     | 24              |
| Triple Cargo Stacking     | 36              |
| Quadruple Cargo Stacking  | 48              |

Total number of nodes required for different setup of **Conveyor Belt Mk. II**.

| Conveyor Belt Mk. II Setup | Number of Nodes |
| -------------------------- | --------------- |
| Base Volume                | 24              |
| Double Cargo Stacking      | 48              |
| Triple Cargo Stacking      | 72              |
| Quadruple Cargo Stacking   | 96              |

Total number of nodes required for different setups of **Conveyor Belt Mk. III**.

| Conveyor Belt Mk. III Setup | Number of Nodes |
| --------------------------- | --------------- |
| Base Volume                 | 60              |
| Double Cargo Stacking       | 120             |
| Triple Cargo Stacking       | 180             |
| Quadruple Cargo Stacking    | 240             |

General formula with **Vein Utilization**

$$
n = \frac{V}{30\cdot\left(1+\frac{k}{10}\right)}
$$

| Symbol | Meaning                                        |
| ------ | ---------------------------------------------- |
| $n$    | Total number of nodes                          |
| $V$    | Transport volume (item per minute)             |
| $k$    | Vein Utilization level                         |
