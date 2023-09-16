# User Manual

## Glossary

**Factory**

A factory is a collection of homogeneous production facilities.

In addition, a number may be included to indicate the quantity of facilities within a factory.
For example, the term "14-Arc Smelter factory" conveys that the factory consists of 14 Arc Smelters.

**I/O Channel**

An I/O channel is a line of conveyor belt.
It either delivers raw materials to a factory or transports products away from it.

## Table Reading Guide

### I/O Tables

The I/O table for [[Annihilation Constraint Sphere]] will be used as an example.

| Channel # | Direction | Item                               | Ratio |
| --------- | --------- | ---------------------------------- | ----- |
| 1         | Input     | [[Particle Container]]             | 1/1   |
| 2         | Input     | [[Processor]]                      | 1/1   |
| 3         | Output    | [[Annihilation Constraint Sphere]] | 1/1   |

Each channel transport exactly one type of item in to or out of the factory.
In this case, there three channels one for [[Particle Container]], [[Processor]] and [[Annihilation Constraint Sphere]].

To give more details about the **Ratio** column, the I/O table for [[Titanium Alloy]] will be used as the next example.

| Channel # | Direction | Item               | Ratio |
| --------- | --------- | ------------------ | ----- |
| 1         | Input     | [[Titanium Ingot]] | 4/4   |
| 2         | Input     | [[Steel]]          | 4/4   |
| 3         | Input     | [[Sulfuric Acid]]  | 4/8   |
| 4         | Input     | [[Sulfuric Acid]]  | 4/8   |
| 5         | Output    | [[Titanium Alloy]] | 4/4   |

There are five channels with channels dedicated to [[Sulfuric Acid]].
Eight units of [[Sulfuric Acid]] is required per production cycle.
Each [[Sulfuric Acid]] channel should only transport four units.

### Reference Table

The Arc Smelter reference table for [[Copper Ingot]] will be used as an example.

| Proliferation            | 360         | 720          | 1800          |
| ------------------------ | ----------- | ------------ | ------------- |
| None                     | `6`         | `12`         | `30`          |
| Extra Products +12.5%    | `5 [337.5]` | `10 [675.0]` | `26 [1755.0]` |
| Extra Products +20%      | `5`         | `10`         | `25`          |
| Extra Products +25%      | `4 [300.0]` | `9 [675.0]`  | `24`          |
| Production Speedup +25%  | `4 [300.0]` | `9 [675.0]`  | `24`          |
| Production Speedup +50%  | `4`         | `8`          | `20`          |
| Production Speedup +100% | `3`         | `6`          | `15`          |

Each cell represents the number of facility required to reach certain production target with different proliferation.
For example, you need a **6-Arc Smelter factory** to reach the production of 360 [[Copper Ingot]]s per minute without proliferation

The numbers in the square brackets represents the highest item production per minute without exceeding the desired target.

It is important to note that these numbers are calculated using the same tier of Conveyor Belt.
At 360 item production per minute, the table assumes each input channel can deliver 360 material per minute.

There are a few cases which are not yet covered, let's use the Assembling Machine Mk.I reference table for [[Deuteron Fuel Rod]] as an example.

| Proliferation            | 360                   | 720                    | 1800                      |
| ------------------------ | --------------------- | ---------------------- | ------------------------- |
| None                     | `(5*9)+3=48`          | `(5*19)+1=96`          | `5*48=240`                |
| Extra Products +12.5%    | `(4*9)+6=42 [354.38]` | `(4*19)+9=85 [717.19]` | `(4*48)+21=213 [1797.19]` |
| Extra Products +20%      | `(4*9)+4=40`          | `(4*19)+4=80`          | `(4*48)+8=200`            |
| Extra Products +25%      | `(4*9)+2=38 [356.25]` | `4*19=76 [712.5]`      | `4*48=192`                |
| Production Speedup +25%  | `(5*7)+3=38 [356.25]` | `(5*15)+1=76 [712.5]`  | `(5*38)+2=192`            |
| Production Speedup +50%  | `(5*6)+2=32`          | `(5*12)+4=64`          | `5*32=160`                |
| Production Speedup +100% | `6*4=24`              | `(5*9)+3=48`           | `5*24=120`                |

Let's focus on producing 360 [[Deuteron Fuel Rod]]s per minute without proliferation and break down each component.

In this case, you need to build five 9-Assembling Machine Mk.I factories and an addition three totaling 48 Assembling Machine Mk.Is to produce 360 [[Deuteron Fuel Rod]] per minute.

## Reference Overview

### Assembler

#### Assembler 1-1

**Recommended recipes:**
- [[Crystal Silicon (advanced)]]
- [[Gear]]
- [[Proliferator Mk.I]]
- [[Space Warper]]
- [[Space Warper (advanced)]]

#### Assembler 2-1

**Recommended recipes:**
- [[Annihilation Constraint Sphere]]
- [[Photon Combiner (advanced)]]
- [[Reinforced Thruster]]
- [[Solar Sail]]

#### Assembler 3-1

**Recommended recipes:**
- [[Circuit Board]]
- [[Dyson Sphere Component]]
- [[Hydrogen Fuel Rod]]
- [[Logistics Drone]]
- [[Magnetic Coil]]
- [[Microcrystalline Component]]
- [[Particle Container]]
- [[Particle Container (advanced)]]
- [[Photon Combiner]]
- [[Plane Filter]]
- [[Plasma Exciter]]
- [[Prism]]
- [[Proliferator Mk.II]]
- [[Proliferator Mk.III]]
- [[Thruster]]
- [[Titanium Glass]]

#### Assembler 4-1

**Recommended recipes:**
- [[Antimatter Fuel Rod]]
- [[Deuteron Fuel Rod]]
- [[Electric Motor]]
- [[Electromagnetic Turbine]] 
- [[Foundation]]
- [[Frame Material]]
- [[Logistics Bot]]
- [[Processor]]
- [[Quantum Chip]]
- [[Small Carrier Rocket]]
- [[Titanium Crystal]]

#### Assembler 5-1

**Recommended recipes:**
- [[Casimir Crystal]]
- [[Casimir Crystal (advanced)]]
- [[Graviton Lens]]
- [[Logistics Vessel]]
- [[Particle Broadband]]

#### Assembler 6-1

**Recommended recipes:**
- [[Super-magnetic Ring]]

### Chemical Facility

#### Chemical Facility 1-2

**Recommended recipes:**
- [[Graphene (advanced)]]

#### Chemical Facility 2-3

**Recommended recipes:**
- [[Hydrogen (Graphene (advanced))]]

#### Chemical Facility 3-1

**Recommended recipes:**
- [[Carbon Nanotube (advanced)]]
- [[Plastic]]

#### Chemical Facility 4-1

**Recommended recipes:**
- [[Carbon Nanotube]]
- [[Graphene]]
- [[Organic Crystal]]

#### Chemical Facility 5-1

**Recommended recipes:**
- [[Sulfuric Acid]]

### Particle Collider

#### Particle Collider 1-2

**Recommended recipes:**
- [[Antimatter]]
- [[Hydrogen (Critical Photon)]]

#### Particle Collider 2-1

**Recommended recipes:**
- [[Deuterium]]

#### Particle Collider 4-1

**Recommended recipes:**
- [[Strange Matter]]

### Refining Facility

#### Refining Facility 1-2

**Recommended recipes:**
- [[Refined Oil]]

#### Refining Facility 2-2

**Recommended recipes:**
- [[Hydrogen (X-Ray Cracking)]]

#### Refining Facility 2-3

**Recommended recipes:**
- [[Hydrogen (Plasma Refining)]]

#### Refining Facility 2-4

**Recommended recipes:**
- [[Energetic Graphite]]

#### Refining Facility 3-1

**Recommended recipes:**
- [[Refined Oil (Reforming Refine)]]

### Research Facility

#### Research Facility 2-1

**Recommended recipes:**
- [[Electromagnetic Matrix]]
- [[Gravity Matrix]]
- [[Structure Matrix]]

#### Research Facility 3-1

**Recommended recipes:**
- [[Information Matrix]]

#### Research Facility 4-1

**Recommended recipes:**
- [[Energy Matrix]]

#### Research Facility 6-1

**Recommended recipes:**
- [[Universe Matrix]]

### Smelting Facility

#### Smelting Facility 1-1

**Recommended recipes**:
- [[Copper Ingot]]
- [[Magnet]]
- [[Iron Ingot]]
- [[Crystal Silicon]]
- [[Diamond]]
- [[Diamond (advanced)]]
- [[Stone Brick]]

#### Smelting Facility 2-1

**Recommended recipes:**
- [[Glass]]
- [[Energetic Graphite]]
- [[High-purity Silicon]]
- [[Titanium Ingot]]

#### Smelting Facility 3-1

**Recommended recipes:**
- [[Steel]]

#### Smelting Facility 4-1

**Recommended recipes:**
- [[Titanium Alloy]]

